import 'dart:async';
import 'dart:convert';
import 'package:app_video_surveillance/splashScreen.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:lottie/lottie.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:typed_data';

import 'Controller.dart';
import 'Get_ip.dart'; // لاستخدام Uint8List

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // -------

  SharedPreferences prefs = await SharedPreferences.getInstance();
  ipAddress = prefs.getString(
        'IP_Address',
      ) ??
      '127.0.0.1:8000';
  serverName = "http://$ipAddress/";
  print('ip=${ipAddress}');
  print('serverName=${serverName}');

  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Real-time Video Feed',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const splashScreen(),
    );
  }
}

class VideoFeedScreen extends StatefulWidget {
  @override
  _VideoFeedScreenState createState() => _VideoFeedScreenState();
}

class _VideoFeedScreenState extends State<VideoFeedScreen> {
  late StreamController<Uint8List?> _frameStreamController;
  late StreamSubscription _frameStreamSubscription;
  Uint8List? _currentFrame; // الصورة الحالية
  Uint8List? _previousFrame; // الصورة السابقة
  String timestamp = "Loading...";

  final String frameUrl = "${serverName}frames";

  @override
  void initState() {
    super.initState();
    _frameStreamController = StreamController<Uint8List?>();
    _startFrameStream();
  }

  void _startFrameStream() {
    _frameStreamSubscription =
        Stream.periodic(const Duration(milliseconds: 100), (_) {
      return _getFrame();
    }).asyncMap((frame) async {
      return await frame;
    }).listen((frame) {
      setState(() {
        if (frame != null && frame.isNotEmpty) {
          _previousFrame = _currentFrame; // تحديث الصورة السابقة
          _currentFrame = frame; // تحديث الصورة الحالية
        }
        // إذا لم يكن هناك إطار جديد، احتفظ بالصورة القديمة.
      });
      _frameStreamController.add(frame);
    });
  }

  Future<Uint8List?> _getFrame() async {
    try {
      final response = await http.get(Uri.parse(frameUrl),headers: myHeaders);

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final frameBase64 = data['frame'];
        final timestampFromApi = data['timestamp'];

        setState(() {
          timestamp = timestampFromApi;
        });

        return base64Decode(frameBase64);
      } else {
        print('Failed to load frame');
        return null;
      }
    } catch (e) {
      print('Error fetching frame: $e');
      return null;
    }
  }

  @override
  void dispose() {
    _frameStreamSubscription.cancel();
    _frameStreamController.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:
            const Text('عرض الفيديو المباشر', textDirection: TextDirection.rtl),
        actions: [
          Lottie.asset(
            'assets/images/video.json', // replace with your Lottie animation file
            width: 100,
            height: 100,
          ),
          IconButton(
              onPressed: () async {
              await  Navigator.of(context).push(
                  PageRouteBuilder(
                    pageBuilder: (context, animation, secondaryAnimation) =>
                        GetIpAddress(),
                    transitionsBuilder:
                        (context, animation, secondaryAnimation, child) {
                      // استخدام FadeTransition مع Tween
                      return FadeTransition(
                        opacity: Tween<double>(
                          begin: 0.0, // يبدأ من الشفافية الكاملة
                          end: 1.0, // ينتهي بدون شفافية
                        ).animate(animation),
                        child: child,
                      );
                    },
                  ),
                );
              setState(() {});
              },
              icon: Icon(Icons.settings)),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Lottie.asset(
              'assets/images/loading.json', // replace with your Lottie animation file
              width: 100,
              height: 100,
            ),
            AnimatedSwitcher(
              duration: const Duration(milliseconds: 300),
              transitionBuilder: (child, animation) {
                return FadeTransition(
                  opacity: Tween<double>(
                    begin: 0.9, // بدء التلاشي من 50% بدلاً من 0
                    end: 1.0, // النهاية عند 100%
                  ).animate(animation),
                  child: child,
                );
              },
              child: _currentFrame != null
                  ? Image.memory(
                      _currentFrame!,
                      key: ValueKey(_currentFrame),
                      width: 320,
                      height: 240,
                      fit: BoxFit.cover,
                    )
                  : _previousFrame != null
                      ? Image.memory(
                          _previousFrame!, // عرض الصورة السابقة
                          key: ValueKey(_previousFrame),
                          width: 320,
                          height: 240,
                          fit: BoxFit.cover,
                        )
                      : const SizedBox(
                          width: 320,
                          height: 240,
                          child: CircularProgressIndicator(), // مؤقت انتظار
                        ),
            ),
            const SizedBox(height: 20),
            Text(
              'الطابع الزمني: $timestamp',
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              textDirection: TextDirection.rtl,
            ),
            const SizedBox(height: 100),
            const Text(
              'إشراف:',
              style: TextStyle(fontWeight: FontWeight.w700),
              textDirection: TextDirection.rtl,
            ),
            const Text(
              'أ.م.د براء إسماعيل',
              textDirection: TextDirection.rtl,
            ),
          ],
        ),
      ),
    );
  }
}

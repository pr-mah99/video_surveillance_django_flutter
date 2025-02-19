import 'dart:async';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter_cache_manager/flutter_cache_manager.dart';
import 'package:lottie/lottie.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'Controller.dart';
import 'SnackBar_Message.dart';

class GetIpAddress extends StatefulWidget {
  GetIpAddress({super.key});


  @override
  State<GetIpAddress> createState() => _GetIpAddressState();
}

class _GetIpAddressState extends State<GetIpAddress> {
  final ipAddressValue = TextEditingController();

  Future<void> Setting_ip(String ip) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    await prefs.setString(
      'IP_Address',
      ip,
    );
    serverName = "http://$serverName/";
  }

// دالة التي تعمل عند فتح النافذة
  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    // getting ip
    ipAddressValue.text = ipAddress;
    // --------
    first();
  }

  Future<void> first() async {
    if(ipAddress !='0.0.0.0'){
    await checkIp();
    // -----
    if(doneChecked){
      Timer(const Duration(seconds: 1), () async {
      await Setting_ip(ipAddressValue.text.trim());
      // ------

      });
    }
  }
  }

  bool loading = false;
  bool doneChecked = false;
  bool isManual = false;

  checkIp() async {
    setState(() {
      loading=true;
      doneChecked = false;
    });

    final client = HttpClient();
    try {
      String url='http://$ipAddress';
      // print('url=$url');
      final request = await client.getUrl(Uri.parse(url));
      request.close();
      final  response = await request.done;
      if (response.statusCode == 200) {
        showMessage('تم الاتصال بين التطبيق والنظام', context);
        setState(() {
          doneChecked = true;
          ipAddressValue.text=ipAddress;
        });
      }
    }catch(e){
      print(e);
      showMessage('فشل الاتصال - تحقق من العنوان الصحيح', context);
    }finally{
      setState(() {
        loading=false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        title: const Text('ألاعدادات'),
        leading: IconButton(
          onPressed:() {
                  Navigator.pop(context);
                },
          icon: const Icon(
            Icons.arrow_back,
          ),
        ),
        actions: [
          ElevatedButton.icon(onPressed: (){
            DefaultCacheManager().emptyCache(); //clears all data (like image or file) in cache.
            // -------
          },label: const Text('أصلاح المشاكل'), icon: const Icon(Icons.verified)),
        ],
      ),
      body: Center(
        child: SingleChildScrollView(
          child: Container(
            margin: const EdgeInsets.all(12),
            padding: const EdgeInsets.all(12),
            child: Column(
              children: [
                const Divider(),
                const Text("أعدادات النظام"),
                const Divider(),
                Center(
                  child:
                  Lottie.asset(
                    'assets/images/video.json', // replace with your Lottie animation file
                    width: 152,
                    height: 152,
                  ),

                ),
                const Text(
                  "أدخل رقم الIP الخاص بمركز البيانات",
                  textDirection: TextDirection.rtl,
                ),
                const SizedBox(
                  height: 10,
                ),

                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Text('https://${ipAddressValue.text}.com / (localhost)'),
                ),

                doneChecked?
                     Icon(Icons.verified,color: Colors.teal.shade600,size: 150,)
                    : Column(
                  children: [
                    isManual == false
                        ? Row(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        IconButton(
                            onPressed: () {
                              setState(() {
                                ipAddress = '';
                                isManual = true;
                              });
                            },
                            icon: const Icon(Icons.clear))
                      ],
                    )
                        : TextFormField(
                      controller: ipAddressValue,
                      keyboardType: TextInputType.emailAddress,
                      decoration: const InputDecoration(
                        hintText: "IP Address",
                        prefixIcon: Icon(
                          Icons.phone_iphone,
                        ),
                      ),
                      onChanged: (String val) {
                        setState(() {
                          ipAddress = val.trim();
                        });
                      },
                    ),

                    const SizedBox(
                      height: 5,
                    ),

                    const Divider(),

                    loading?
                    const Padding(
                      padding: EdgeInsets.all(18.0),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          CircularProgressIndicator(),
                          SizedBox(width: 10,),
                          Text('جار التحقق'),
                        ],
                      ),
                    )
                        :

                    ElevatedButton.icon(
                      onPressed: checkIp,
                      label: const Text("تحقق"),
                      icon: const Icon(Icons.check),
                    ),


                  ],
                ),


                const Divider(),
                const SizedBox(
                  height: 10,
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    ElevatedButton.icon(
                      onPressed: doneChecked
                          ? () async {
                              await Setting_ip(ipAddressValue.text.trim());
                              setState(() {});
                      }
                          : null,
                      label: const Padding(
                        padding: EdgeInsets.symmetric(horizontal: 25.0,vertical: 10),
                        child: Text("حفظ الاعددات ألان"),
                      ),
                      icon: const Icon(Icons.save),
                    ),
                    const SizedBox(
                      height: 10,
                    ),
                    IconButton(
                        onPressed: () {
                          setState(() {
                            isManual = true;
                            doneChecked=false;
                          });
                        },
                        icon: const Icon(Icons.clear))

                  ],
                ),
                const SizedBox(
                  height: 10,
                ),
                const Divider(),
                const Divider(),

                const SizedBox(
                  height: 10,
                ),
                const Divider(),
                const Text('يمكنك التخطي ولكن تذكر يجب الاتصال لتحديث البيانات'),
                const Divider(),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

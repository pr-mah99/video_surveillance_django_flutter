import 'package:flutter/material.dart';

void showMessage(String? message, BuildContext? context) {
  ScaffoldMessenger.of(context!).removeCurrentSnackBar(); //حذف الرسالة الحالية اذا وجدت
  ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      content: Text(
        message!,
        style: const TextStyle(color: Colors.white,fontWeight: FontWeight.w700),
      ),
      behavior: SnackBarBehavior.floating,
      action: SnackBarAction(
        label: 'موافق',
        textColor: Colors.white,
        disabledTextColor:Colors.white,
        onPressed: () {
          // Some code to undo the change.
        },
      ),
      // backgroundColor: Colors.teal
      backgroundColor: Theme.of(context).primaryColor
  ));
}

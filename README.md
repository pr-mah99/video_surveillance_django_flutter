# video_surveillance_django_flutter
مشروع video_مشروع video_surveillance_django_flutter هو نظام مراقبة فيديو متكامل يعتمد على تقنيات الويب والهواتف المحمولة، حيث يجمع بين قوة إطار العمل Django للتعامل مع الخلفية (Backend) وإطار العمل Flutter لتطوير واجهة المستخدم الأمامية (Frontend). الهدف من المشروع هو توفير حل شامل لإدارة أنظمة المراقبة عبر الإنترنت.


<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Video Surveillance Project</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f9;
      color: #333;
      line-height: 1.6;
    }

    header {
      background-color: #007BFF;
      color: white;
      padding: 20px;
      text-align: center;
    }

    .container {
      max-width: 1200px;
      margin: 20px auto;
      padding: 20px;
      background: white;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1, h2, h3 {
      color: #007BFF;
    }

    .language-switch {
      text-align: center;
      margin-bottom: 20px;
    }

    .language-switch button {
      padding: 10px 20px;
      margin: 5px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      background-color: #007BFF;
      color: white;
      font-size: 16px;
    }

    .language-switch button:hover {
      background-color: #0056b3;
    }

    .content-ar, .content-en {
      display: none;
    }

    .active {
      display: block;
    }

    footer {
      text-align: center;
      padding: 10px;
      background-color: #007BFF;
      color: white;
      position: fixed;
      bottom: 0;
      width: 100%;
    }
  </style>
</head>
<body>

  <header>
    <h1>Video Surveillance Application in Wireless Multimedia Sensor Networks</h1>
    <p>طئاسولا ةددعتملا ةيكلسلالا راعشتسلاا تاكبش يف ويديفلاب</p>
  </header>

  <div class="container">
    <div class="language-switch">
      <button onclick="switchLanguage('en')">English</button>
      <button onclick="switchLanguage('ar')">Arabic</button>
    </div>

    <!-- English Content -->
    <div class="content-en active">
      <h2>Introduction</h2>
      <p>This project aims to develop an efficient compressed sensing-based security approach for video surveillance applications in wireless multimedia sensor networks.</p>

      <h2>Features</h2>
      <ul>
        <li>Video Compression: Reduces video data size by up to 85% while maintaining acceptable quality.</li>
        <li>Data Encryption: Uses AES encryption to secure data during transmission and storage.</li>
        <li>Cross-Platform Support: Works on Android, iOS, Windows, macOS, and web browsers.</li>
        <li>RESTful API: Built using Django to facilitate communication between the system and other applications.</li>
      </ul>

      <h2>Installation</h2>
      <pre>
# Set up environment
python -m venv venv
.\venv\Scripts\Activate  # For Windows
source venv/bin/activate  # For Linux/MacOS

# Install dependencies
pip install django
pip install djangorestframework
pip install opencv-python
pip install pycryptodome
pip install numpy scipy Pillow
pip install requests
pip install moviepy pyaudio

# Create a new project
django-admin startproject video_surveillance
cd video_surveillance
python manage.py startapp surveillance

# Migrate models to database
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
      </pre>
    </div>

    <!-- Arabic Content -->
    <div class="content-ar">
      <h2>المقدمة</h2>
      <p>يهدف هذا المشروع إلى تطوير نظام مراقبة فيديو فعال وآمن باستخدام تقنيات ضغط الفيديو والتشفير المتقدم في شبكات الاستشعار اللاسلكية المتعددة الوسائط.</p>

      <h2>الميزات</h2>
      <ul>
        <li>ضغط الفيديو: يقلل حجم بيانات الفيديو بنسبة تصل إلى 85% مع الحفاظ على جودة مقبولة.</li>
        <li>التشفير: يستخدم خوارزمية AES لتامين البيانات أثناء النقل والتخزين.</li>
        <li>دعم متعدد المنصات: يعمل على Android، iOS، Windows، macOS، ومتصفحات الويب.</li>
        <li>واجهة برمجية (API): مبنية باستخدام Django لتسهيل التواصل بين النظام والتطبيقات الأخرى.</li>
      </ul>

      <h2>التثبيت</h2>
      <pre>
# إعداد البيئة
python -m venv venv
.\venv\Scripts\Activate  # لنظام Windows
source venv/bin/activate  # لنظام Linux/MacOS

# تثبيت المتطلبات
pip install django
pip install djangorestframework
pip install opencv-python
pip install pycryptodome
pip install numpy scipy Pillow
pip install requests
pip install moviepy pyaudio

# إنشاء مشروع جديد
django-admin startproject video_surveillance
cd video_surveillance
python manage.py startapp surveillance

# رحيل النماذج إلى قاعدة البيانات
python manage.py makemigrations
python manage.py migrate

# تشغيل السيرفر
python manage.py runserver
      </pre>
    </div>
  </div>

  <footer>
    &copy; 2024 Video Surveillance Project | All Rights Reserved
  </footer>

  <script>
    function switchLanguage(lang) {
      const contentEn = document.querySelector('.content-en');
      const contentAr = document.querySelector('.content-ar');

      if (lang === 'en') {
        contentEn.classList.add('active');
        contentAr.classList.remove('active');
      } else if (lang === 'ar') {
        contentAr.classList.add('active');
        contentEn.classList.remove('active');
      }
    }
  </script>

</body>
</html>
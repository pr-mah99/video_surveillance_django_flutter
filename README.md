# video_surveillance_django_flutter
مشروع video_مشروع video_surveillance_django_flutter هو نظام مراقبة فيديو متكامل يعتمد على تقنيات الويب والهواتف المحمولة، حيث يجمع بين قوة إطار العمل Django للتعامل مع الخلفية (Backend) وإطار العمل Flutter لتطوير واجهة المستخدم الأمامية (Frontend). الهدف من المشروع هو توفير حل شامل لإدارة أنظمة المراقبة عبر الإنترنت.


  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f9;
      color: #333;
      line-height: 1.6;
      direction: rtl; /* Right-to-left for Arabic */
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

    footer {
      text-align: center;
      padding: 10px;
      background-color: #007BFF;
      color: white;
      position: fixed;
      bottom: 0;
      width: 100%;
    }

    pre {
      background-color: #f9f9f9;
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #ddd;
      overflow-x: auto;
    }
  </style>

  <header>
    <h1>مشروع مراقبة الفيديو في شبكات الاستشعار اللاسلكية المتعددة الوسائط</h1>
    <!-- Header in English: Video Surveillance Application in Wireless Multimedia Sensor Networks -->
  </header>

  <div class="container">
    <h2>المقدمة</h2>
    <!-- Introduction in English -->
    <p>شهدت تقنية مراقبة الفيديو تطوراً سريعاً أدى إلى انتشار شبكات الاستشعار اللاسلكية المتعددة الوسائط (WMSNs). هذه الشبكات حيوية للعديد من التطبيقات مثل الأمن والمراقبة والبنية التحتية للمدن الذكية. ومع ذلك، فإن زيادة حجم بيانات الفيديو تثير تحديات كبيرة تتعلق بتخزين البيانات ونقلها وأمانها. يقدم هذا المشروع نهجاً فعالاً باستخدام تقنيات ضغط البيانات وطرق تشفير قوية لتحسين كفاءة وأمان أنظمة مراقبة الفيديو.</p>

    <h2>مشكلة البحث</h2>
    <!-- Research Problem in English -->
    <p>التحدي الرئيسي الذي يتناوله هذا المشروع هو نقل وتخزين كميات كبيرة من بيانات الفيديو في شبكات الاستشعار اللاسلكية التي غالباً ما تعاني من قيود في النطاق الترددي والطاقة. بالإضافة إلى ذلك، هناك حاجة متزايدة لتدابير أمان قوية لحماية المعلومات الحساسة من الوصول غير المصرح به والهجمات. يهدف هذا المشروع إلى معالجة هذه القضايا من خلال تطوير نظام يقوم بضغط إطارات الفيديو وتشفيرها قبل الإرسال، مما يقلل من حجم البيانات ويعزز الأمان أثناء النقل.</p>

    <h2>أهداف البحث</h2>
    <!-- Research Objectives in English -->
    <p>تكمن أهمية هذا البحث في إمكاناته لتعزيز كفاءة وأمان أنظمة مراقبة الفيديو. مع استمرار توسع المناطق الحضرية، تتزايد الحاجة إلى حلول مراقبة فعالة. يساهم هذا المشروع ليس فقط في المجال الأكاديمي لشبكات الاستشعار المتعددة الوسائط، بل يقدم أيضاً حلولاً عملية لتطبيقات العالم الحقيقي في مجالات الأمن والمراقبة، مما يجعله ذا قيمة لتحسين أداء المراقبة وزيادة مستوى الحماية.</p>

    <h2>منهجية البحث</h2>
    <!-- Methodology in English -->
    <p>تتضمن المنهجية المستخدمة في هذا البحث عدة خطوات رئيسية:</p>
    <ol>
      <li>جمع البيانات: التقاط إطارات الفيديو باستخدام كاميرا متكاملة مع شبكة الاستشعار اللاسلكية.</li>
      <li>ضغط البيانات: تنفيذ ضغط JPEG لتقليل حجم إطارات الفيديو.</li>
      <li>تشفير البيانات: استخدام خوارزمية AES لتشفير بيانات الإطارات المضغوطة.</li>
      <li>نقل البيانات: إرسال البيانات المشفرة إلى الخادم لتخزينها ومعالجتها.</li>
      <li>استرجاع البيانات: توفير واجهة برمجية (API) لاسترجاع بيانات إطارات الفيديو عند الحاجة.</li>
    </ol>

    <h2>الأدوات والتكنولوجيا المستخدمة</h2>
    <!-- Tools and Technologies in English -->
    <ul>
      <li>لغة البرمجة: بايثون.</li>
      <li>الإطار: Django لتطوير واجهة برمجية (API).</li>
      <li>المكتبات: OpenCV لمعالجة الفيديو، Crypto للتشفير، وRequests للتواصل عبر HTTP.</li>
      <li>قاعدة البيانات: Django ORM لإدارة تخزين بيانات إطارات الفيديو.</li>
    </ul>

    <h2>التثبيت</h2>
    <!-- Installation in English -->
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
from django.conf import settings
from django.http import JsonResponse

class ApiKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # التحقق إذا كان الرابط يحتوي على 'frames'
        if request.path.startswith('/frames/'):
            api_key = request.headers.get('X-API-KEY')  # استخراج المفتاح من Headers
            if api_key != settings.API_SECRET_KEY:
                return JsonResponse({'error': 'Unauthorized'}, status=401)

        response = self.get_response(request)
        return response

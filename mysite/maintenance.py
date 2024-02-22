from django.http import HttpResponse
from django.conf import settings

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.MAINTENANCE_MODE:
            return HttpResponse("Our website is under maintenance. Please check back later.")
        else:
            response = self.get_response(request)
            return response
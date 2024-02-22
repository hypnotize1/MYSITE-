from django.http import HttpResponse
from django.shortcuts import render


from django.shortcuts import render

def coming_soon(request):
    return render(request, 'coming_soon.html',)
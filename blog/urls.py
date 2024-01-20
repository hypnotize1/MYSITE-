from django.urls import URLPattern, path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name = 'index'),
    path('single', blog_single, name = 'single'),
    path('test', test_func, name = 'test')
]
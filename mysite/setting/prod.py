from mysite.settings import *

CSRF_COOKIE_SECURE = True

MEDIA_ROOT = '/home/hypnotiz/public_html/media'
STATIC_ROOT = '/home/hypnotiz/public_html/static'
STATICFILES_DIRS = [
    BASE_DIR / "statics" ,
]

SITE_ID = 3

# INSTALLED_APPS = []

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hypnotiz_travel',
        'USER': 'hypnotiz_hossein',
        'PASSWORD': 'hosseinseyfi80',
        'HOST': 'localhost',
        'PORT': '3306',        
    }
}

ALLOWED_HOSTS = ['hypnotize1.ir', 'www.hypnotize1.ir']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f5r6d%ff3s1c3lvm3@b_bpua@!@)&irhpjdqc*230-g9e1g%!$'

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'

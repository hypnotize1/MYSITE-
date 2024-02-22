from mysite.settings import *

CSRF_COOKIE_SECURE = True

MEDIA_ROOT = BASE_DIR / 'media' 
STATIC_ROOT = BASE_DIR / 'static'

STATICFILES_DIRS = [
    BASE_DIR / "statics" ,
]

SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# INSTALLED_APPS = []

ALLOWED_HOSTS = ['hypnotize1.ir', 'www.hypnotize1.ir']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f5r6d%ff3s1c3lvm3@b_bpua@!@)&irhpjdqc*230-g9e1g%!$'

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# إعدادات القوالب
TEMPLATE_DIR = os.path.join(BASE_DIR, "apps", "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your_secret_key')

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # إضافة النطاقات الخاصة بك هنا

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.bookmodule',
    'apps.usermodule',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'new_libraryproject.urls'

WSGI_APPLICATION = 'new_libraryproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# إعدادات الملفات الثابتة (Static Files)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "apps", "static")]

# إعدادات ملفات الميديا (Media Files) لعرض الصور
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

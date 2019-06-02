"""
Django settings for Django1 project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')%0*nr26c=)!$#0ia(mz7dzq+0j!nmt(sn9u*t3#lck%ot2nuf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig',
    'stuDatabase',  # 在同步的时候需要使用到 表结构发生变化会进行自动同步
    'l_session',
    'l_auth',
    'blog',
    'uploadFile',
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

ROOT_URLCONF = 'Django1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'html')],  # 告诉django html文件夹的位置
        'APP_DIRS': True,  # 设置成 True则不仅会在dirs中查找文件，还会在app_dirs中去查找templates文件夹
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

WSGI_APPLICATION = 'Django1.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'study_django',  # 数据库名字(需要先创建)
        'USER': 'root',  # 登录用户名
        'PASSWORD': 'zhou123',  # 密码
        'HOST': 'localhost',  # 数据库IP地址,留空默认为localhost
        'PORT': 3306,  # 端口
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# STATIC_URL = '/static/'
#
# STATIC_ROOT = os.path.join(BASE_DIR,'static').replace('\\', '/')
# STATIC_DIRS = (
#     ('css',os.path.join(STATIC_ROOT,'css').replace('\\', '/')),
#     ('images',os.path.join(STATIC_ROOT,'images').replace('\\', '/'))
# )

STATIC_URL = '/static/'
# HERE = os.path.dirname(os.path.abspath(__file__))
# HERE = os.path.join(HERE, '../')
# 取消一下注释则可以在整个项目中使用static
# STATICFILES_DIRS = (
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
#     os.path.join(BASE_DIR, 'static/'),
# )
AUTH_USER_MODEL='blog.UserInfo' # 用来配置auth_user继承

MEDIA_ROOT = os.path.join(BASE_DIR,'blog','media')  # 指定media路径
MEDIA_URL = '/media/'

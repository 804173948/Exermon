"""
Django settings for ExermonServer project.

Generated by 'django-admin startproject' using Django 2.1.8.

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
SECRET_KEY = ''

AUTH_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]

HTML_TEST = True

# Application definition

FILE_UPLOAD_MAX_MEMORY_SIZE = 26214400  #上传文件大小，改成25M
DATA_UPLOAD_MAX_MEMORY_SIZE = 26214400	#上传数据大小，也改成了25M

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'xadmin',
    'crispy_forms',
    'reversion',

    'game_module',
    'player_module',
    'item_module',
    'exermon_module',
    'question_module',
    'record_module',
    'season_module',
    'battle_module',

	'english_pro_module',

    'werkzeug_debugger_runserver',
    'django_extensions',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ExermonServer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'ExermonServer.wsgi.application'
ASGI_APPLICATION = "ExermonServer.routing.application"

# Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'exermon',  # 使用的数据库的名字
        'USER': 'root',  # MySQL中的用户名
        'PASSWORD': '',  # 登录MySQL的密码
        'HOST': 'localhost',  # MySQL数据库所在的主机的ip
        'PORT': 3306,  # MySQL服务的端口号
        'OPTIONS': {
            "init_command": "SET default_storage_engine='INNODB'"
        }
    }
}
DATABASES['default']['OPTIONS']['init_command'] = "SET sql_mode='STRICT_TRANS_TABLES'"#排除错误

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

LANGUAGE_CODE = 'zh-hans'    # 中文

TIME_ZONE = 'Asia/Shanghai'  # 中国上海时区

USE_I18N = True

USE_L10N = True

USE_TZ = False

SECURE_SSL_REDIRECT = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_BASE = 'static'

# 登陆验证

#EMAIL_USE_SSL = True
EMAIL_USE_TLS = True

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '' # 帐号
EMAIL_HOST_PASSWORD = ''  # 密码

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SMS_API_KEY = ''
SMS_SEND_URL = 'https://sms.yunpian.com/v2/sms/single_send.json'

CODE_LENGTH = 6
CODE_SECOND = 60

CODE_TEXT = {
    'register': ('Exermon','亲爱的%s，\n您的 Exermon 注册验证码为 %s \n验证码将在 %d 秒后失效。\n若非本人操作请忽略。',DEFAULT_FROM_EMAIL),
    'retrieve': ('Exermon','亲爱的%s，\n您的 Exermon 重置密码验证码为 %s \n验证码将在 %d 秒后失效。\n若非本人操作请忽略。',DEFAULT_FROM_EMAIL)
}
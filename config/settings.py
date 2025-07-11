"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

from keys import SECRET_KEY_value

SECRET_KEY = SECRET_KEY_value

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

    'blog.apps.BlogConfig',
    'api.apps.ApiConfig',

    'rest_framework',
    'rest_framework.authtoken',     # We add this line from drf tokenAuthentication

    'dj_rest_auth',                 # for dj-rest-auth
    'dj_rest_auth.registration',    # for dj-rest-auth
    'django.contrib.sites',         # for dj-rest-auth

    'allauth',                      # for dj-rest-auth
    'allauth.account',              # for dj-rest-auth
    'allauth.socialaccount',        # for dj-rest-auth

]

# This is for dj-rest-auth
SITE_ID = 1


# MiddleWare is a tool which is called after each request or refresh
MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',                #   a csrf allocated to our request(header) and another is allocated to our form data, If the csrfs were equals then it's ok. otherwise it's not ok and the tasks doesn't complete
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# FOR SETTING REST FRAMEWORK WE ADDED HERE #################################
REST_FRAMEWORK = {
    # we can use third-party permission packages
    # These permissions are general during the project. For specific permissions we set them in their own api views method
    'DEFAULT_PERMISSION_CLASSES': [
        'api.permissions.IsStaffOrReadOnly',                         # I created a permissions file which has my own customized permissions!!
        # 'rest_framework.permissions.IsAuthenticated',                 # this is a permission which only shows the apis details when the user logged in and it works here and doesn't need to do anything
        # 'rest_framework.permissions.IsAdminUser',                    # You can set different permission here. check the rest framework documentation
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',     # authenticated users can change the articles and stuff but not-authenticated users only can read the articles
    ]   ,

# These authentications are general during the project. For specific authentications we set them in their own api views method
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',        # BasicAuthentication is not recommended for production!!! it's only for testing if some permissions work okay like IsAuthenticated
        # 'rest_framework.authentication.SessionAuthentication',        # SessionAuthentication is for production but used for only websites and not android app and other things. The session should be in same device and browser even!!!
        'rest_framework.authentication.TokenAuthentication',            # We also add 'rest_framework.authtoken' to installed app above!!!
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # jwt
        # knox
        # oauth
    ]   ,

}

# FOR dj-rest-auth REGISTRATION EMAIL FIELD WE NEED TO ADD THIS LINE
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'        # For dj-rest-auth registration email field we need to add this line'


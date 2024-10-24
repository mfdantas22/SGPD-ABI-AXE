

import os, random, string, inspect
from pathlib import Path
from dotenv import load_dotenv
from str2bool import str2bool

import django_dyn_dt

load_dotenv()  # take environment variables from .env.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = ''.join(random.choice( string.ascii_lowercase  ) for i in range( 32 ))

# Enable/Disable DEBUG Mode
DEBUG = str2bool(os.environ.get('DEBUG'))
#print(' DEBUG -> ' + str(DEBUG) ) 

ALLOWED_HOSTS = ['*']

# Add here your deployment HOSTS
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://localhost:5085', 'http://127.0.0.1:8000', 'http://127.0.0.1:5085']

X_FRAME_OPTIONS = "SAMEORIGIN"

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'admin_datta.apps.AdminDattaConfig',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "abi",

    # Tooling Dynamic_DT
    'django_dyn_dt',             # <-- NEW: Dynamic_DT

    # Tooling API-GEN
    'django_api_gen',            # Django API GENERATOR  # <-- NEW
    'rest_framework',            # Include DRF           # <-- NEW 
    'rest_framework.authtoken',  # Include DRF Auth      # <-- NEW     
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

HOME_TEMPLATES      = os.path.join(BASE_DIR, 'abi/templates')
TEMPLATE_DIR_DATATB = os.path.join(BASE_DIR, "django_dyn_dt/templates") # <-- NEW: Dynamic_DT

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [HOME_TEMPLATES, TEMPLATE_DIR_DATATB],                  # <-- UPD: Dynamic_DT
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Backend do MySQL
        'NAME': 'sgpd_abiaxe',                        # Nome do banco de dados
        'USER': 'root',                        # Usuário do banco de dados
        'PASSWORD': 'root',                    # Senha do usuário
        'HOST': 'localhost',                   # Endereço do servidor, geralmente localhost
        'PORT': '3306',                        # Porta do MySQL, 3306 é a padrão
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "UTf-8"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DYN_DB_PKG_ROOT = os.path.dirname( inspect.getfile( django_dyn_dt ) ) # <-- NEW: Dynamic_DT

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(DYN_DB_PKG_ROOT, "templates/static"),                # <-- NEW: Dynamic_DT 
)

#if not DEBUG:
#    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = '/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ### DYNAMIC_DATATB Settings ###
DYNAMIC_DATATB = {
    # SLUG -> Import_PATH 
    'product'  : "abi.models.Product",
}
########################################

# ### API-GENERATOR Settings ###
API_GENERATOR = {
    # SLUG -> Import_PATH 
    'product'  : "abi.models.Product",
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}
########################################
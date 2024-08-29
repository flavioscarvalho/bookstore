import os
from pathlib import Path
from dotenv import load_dotenv

# Define o caminho para o arquivo .env.dev
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / '.env.dev'
print(f"Loading .env file from {dotenv_path}")

# Carregar as variáveis de ambiente do arquivo .env.dev
load_dotenv(dotenv_path)

# Definir as variáveis de ambiente
DEBUG = os.getenv('DEBUG', '1').lower() in ["1", "true"]

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-_uql)*)q-k=yx15(*vw#ii-r7p_342(4viiznmi68+^cx=65tm')

# Configurar ALLOWED_HOSTS com valores padrão e permitir localhost e 0.0.0.0
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1,[::1]').split(',')

# Adiciona 'localhost' sem porta, para evitar erros de host
if 'localhost' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append('localhost')

# Adiciona 'localhost:8000' explicitamente para resolver o problema de DisallowedHost
if 'localhost:8000' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append('localhost:8000')

# Adiciona '0.0.0.0' para aceitar todas as conexões
if '0.0.0.0' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append('0.0.0.0')

# Adiciona '127.0.0.1:8000' se estiver faltando
if '127.0.0.1:8000' not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append('127.0.0.1:8000')

SQL_ENGINE = os.getenv('SQL_ENGINE', 'django.db.backends.postgresql')
SQL_DATABASE = os.getenv('SQL_DATABASE', 'bookstore_dev_db')
SQL_USER = os.getenv('SQL_USER', 'bookstore_dev')
SQL_PASSWORD = os.getenv('SQL_PASSWORD', 'bookstore_dev')
SQL_HOST = os.getenv('SQL_HOST', 'localhost')  # Manter como 'localhost' para configuração local
SQL_PORT = os.getenv('SQL_PORT', '5432')

# Configurações do Django
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "order",
    "product",
    "rest_framework",
    "rest_framework.authtoken",
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "bookstore.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "bookstore.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': os.getenv('SQL_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('SQL_DATABASE', 'bookstore_db'),
        'USER': os.getenv('SQL_USER', 'bookstore'),
        'PASSWORD': os.getenv('SQL_PASSWORD', 'bookstore'),
        'HOST': os.getenv('SQL_HOST', 'db'),
        'PORT': os.getenv('SQL_PORT', '5432'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INTERNAL_IPS = [
    "127.0.0.1",
]

# Debug output
print("DEBUG:", DEBUG)
print("SECRET_KEY:", SECRET_KEY)
print("DJANGO_ALLOWED_HOSTS:", ALLOWED_HOSTS)
print("SQL_ENGINE:", SQL_ENGINE)
print("SQL_DATABASE:", SQL_DATABASE)
print("SQL_USER:", SQL_USER)
print("SQL_HOST:", SQL_HOST)
print("SQL_PORT:", SQL_PORT)

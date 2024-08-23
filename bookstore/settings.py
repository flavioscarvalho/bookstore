# import os
# from pathlib import Path
# from typing import List
# import dotenv

# # Carregar as variáveis de ambiente do arquivo .env.dev
# dotenv.load_dotenv(".env.dev")

# # Diretório base do projeto
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Chave secreta para a aplicação Django
# SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-_uql)*)q-k=yx15(*vw#ii-r7p_342(4viiznmi68+^cx=65tm")

# # Modo de depuração (True para desenvolvimento, False para produção)
# DEBUG = int(os.environ.get("DEBUG", default=1))

# # Hosts permitidos para acessar a aplicação
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# # Aplicações instaladas
# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     "django_extensions",
#     "order",
#     "product",
#     "rest_framework",
#     "rest_framework.authtoken",
#     "debug_toolbar",
# ]

# # Middlewares configurados
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]

# # Configuração de URL raiz
# ROOT_URLCONF = "bookstore.urls"

# # Configuração dos templates
# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

# # Configuração WSGI
# WSGI_APPLICATION = "bookstore.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
#         "NAME": os.environ.get("SQL_DATABASE", str(BASE_DIR / "db.sqlite3")),
#         "USER": os.environ.get("SQL_USER", "user"),
#         "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
#         "HOST": os.environ.get("SQL_HOST", "localhost"),
#         "PORT": os.environ.get("SQL_PORT", "5432"),
#         "OPTIONS": {
#             "options": "-c client_encoding=UTF8",
#         },
#     }
# }

# # Validações de senha
# AUTH_PASSWORD_VALIDATORS = [
#     {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
#     {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
#     {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
#     {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
# ]

# # Configurações de internacionalização
# LANGUAGE_CODE = "pt-br"
# TIME_ZONE = "America/Sao_Paulo"
# USE_I18N = True
# USE_L10N = True
# USE_TZ = True

# # Configuração dos arquivos estáticos
# STATIC_URL = "static/"

# # Configuração do campo de chave primária padrão
# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# # IPs internos para ferramentas de depuração
# INTERNAL_IPS = [
#     "127.0.0.1",
# ]

# print("DB CONFIG:", os.environ.get("SQL_USER"), os.environ.get("SQL_PASSWORD"))

# import os

# # Carregar as variáveis de ambiente do arquivo .env
# dotenv.load_dotenv()

# BASE_DIR = Path(__file__).resolve().parent.parent

# print("DEBUG:", os.environ.get("DEBUG"))
# print("SECRET_KEY:", os.environ.get("SECRET_KEY"))
# print("DJANGO_ALLOWED_HOSTS:", os.environ.get("DJANGO_ALLOWED_HOSTS"))
# print("SQL_ENGINE:", os.environ.get("SQL_ENGINE"))
# print("SQL_DATABASE:", os.environ.get("SQL_DATABASE"))
# print("SQL_USER:", os.environ.get("SQL_USER"))
# print("SQL_PASSWORD:", os.environ.get("SQL_PASSWORD"))
# print("SQL_HOST:", os.environ.get("SQL_HOST"))
# print("SQL_PORT:", os.environ.get("SQL_PORT"))


import os
from pathlib import Path
from dotenv import load_dotenv

# Define o caminho para o arquivo .env.dev
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / 'env.dev'
print(f"Loading .env file from {dotenv_path}")

# Carregar as variáveis de ambiente do arquivo .env.dev
load_dotenv(dotenv_path)

# Definir as variáveis de ambiente
# Corrigido o DEBUG para interpretar corretamente "True", "False", "1" e "0"
DEBUG = os.getenv('DEBUG', '1') in ["1", "True", "true"]

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-_uql)*)q-k=yx15(*vw#ii-r7p_342(4viiznmi68+^cx=65tm')

# Configurar ALLOWED_HOSTS com valores padrão e permitir localhost:8000
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1,[::1]').split(',')
ALLOWED_HOSTS += ['localhost:8000']  # Adicionar localhost:8000 se não estiver na lista

SQL_ENGINE = os.getenv('SQL_ENGINE', 'django.db.backends.postgresql')
SQL_DATABASE = os.getenv('SQL_DATABASE', 'bookstore_dev_db')
SQL_USER = os.getenv('SQL_USER', 'bookstore_dev')
SQL_PASSWORD = os.getenv('SQL_PASSWORD', 'bookstore_dev')
SQL_HOST = os.getenv('SQL_HOST', 'db')
SQL_PORT = os.getenv('SQL_PORT', '5432')

# Debug output
print("DEBUG:", DEBUG)
print("SECRET_KEY:", SECRET_KEY)
print("DJANGO_ALLOWED_HOSTS:", ALLOWED_HOSTS)
print("SQL_ENGINE:", SQL_ENGINE)
print("SQL_DATABASE:", SQL_DATABASE)
print("SQL_USER:", SQL_USER)
print("SQL_PASSWORD:", SQL_PASSWORD)
print("SQL_HOST:", SQL_HOST)
print("SQL_PORT:", SQL_PORT)

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
        'NAME': os.getenv('SQL_DATABASE', 'bookstore_dev_db'),
        'USER': os.getenv('SQL_USER', 'bookstore_dev'),
        'PASSWORD': os.getenv('SQL_PASSWORD', 'bookstore_dev'),
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

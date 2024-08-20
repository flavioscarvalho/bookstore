import os
from pathlib import Path
from typing import List
import dotenv

# Carregar as variáveis de ambiente do arquivo .env.dev
dotenv.load_dotenv(".env.dev")

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta para a aplicação Django
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-_uql)*)q-k=yx15(*vw#ii-r7p_342(4viiznmi68+^cx=65tm")

# Modo de depuração (True para desenvolvimento, False para produção)
DEBUG = int(os.environ.get("DEBUG", default=1))

# Hosts permitidos para acessar a aplicação
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# Aplicações instaladas
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

# Middlewares configurados
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

# Configuração de URL raiz
ROOT_URLCONF = "bookstore.urls"

# Configuração dos templates
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

# Configuração WSGI
WSGI_APPLICATION = "bookstore.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
        "OPTIONS": {
            "options": "-c client_encoding=UTF8",
        },
    }
}



# Validações de senha
AUTH_PASSWORD_VALIDATORS = [
    {"NAME":
     "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
     },
    {"NAME":
     "django.contrib.auth.password_validation.MinimumLengthValidator"
     },
    {"NAME":
     "django.contrib.auth.password_validation.CommonPasswordValidator"
     },
    {"NAME":
     "django.contrib.auth.password_validation.NumericPasswordValidator"
     },
]

# Configurações de internacionalização
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Configuração dos arquivos estáticos
STATIC_URL = "static/"

# Configuração do campo de chave primária padrão
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# IPs internos para ferramentas de depuração
INTERNAL_IPS = [
    "127.0.0.1",
]


print("DB CONFIG:", os.environ.get("SQL_USER"), os.environ.get("SQL_PASSWORD"))

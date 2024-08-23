import os
from dotenv import load_dotenv
from pathlib import Path

# Define o caminho para o arquivo env.dev
dotenv_path = Path(__file__).resolve().parent / ".env.dev"
print(f"Loading .env file from {dotenv_path}")

# Carregar as variáveis de ambiente do arquivo env.dev
load_dotenv(dotenv_path)

# Verificar se as variáveis de ambiente estão sendo carregadas
print("DEBUG:", os.getenv("DEBUG"))
print("SECRET_KEY:", os.getenv("SECRET_KEY"))
print("DJANGO_ALLOWED_HOSTS:", os.getenv("DJANGO_ALLOWED_HOSTS"))
print("SQL_ENGINE:", os.getenv("SQL_ENGINE"))
print("SQL_DATABASE:", os.getenv("SQL_DATABASE"))
print("SQL_USER:", os.getenv("SQL_USER"))
print("SQL_PASSWORD:", os.getenv("SQL_PASSWORD"))
print("SQL_HOST:", os.getenv("SQL_HOST"))
print("SQL_PORT:", os.getenv("SQL_PORT"))

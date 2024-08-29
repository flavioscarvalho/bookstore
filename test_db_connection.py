import psycopg2
from dotenv import load_dotenv
import os
from pathlib import Path

# Carregar o arquivo .env
dotenv_path = Path("C:/Users/profe/Desktop/BOOKSTORE/.env.dev")
load_dotenv(dotenv_path=dotenv_path)

# Obter variáveis de ambiente
database = os.getenv('SQL_DATABASE', 'bookstore_dev_db')
user = os.getenv('SQL_USER', 'bookstore_dev')
password = os.getenv('SQL_PASSWORD', 'bookstore_dev')
host = os.getenv('SQL_HOST', 'localhost')
port = os.getenv('SQL_PORT', '5432')

print(f"Conectando ao banco de dados {database} como usuário {user}")

try:
    # Estabelecendo a conexão com o banco de dados
    connection = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host,
        port=port,
        options="-c client_encoding=UTF8"  # Forçar uso de UTF-8 na conexão
    )
    print("Conexão estabelecida com sucesso.")

    # Fechando a conexão após o uso
    connection.close()

except psycopg2.DatabaseError as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

except UnicodeDecodeError as e:
    print(f"Erro de codificação: {e}")

except Exception as e:
    print(f"Erro inesperado: {e}")

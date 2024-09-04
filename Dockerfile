# `python-base` sets up all our shared environment variables
FROM python:3.12.2-slim AS python-base

# Definindo variáveis de ambiente para Python, pip e Poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Adicionando Poetry e venv ao PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instalando dependências necessárias
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev gcc \
        python3-dev \
        python3-pip \
    && pip install psycopg2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalando o Poetry - respeitando $POETRY_VERSION e $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=$POETRY_VERSION python3 -

# Configurando o diretório de trabalho e copiando os arquivos de requisitos do projeto
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Instalando as dependências do projeto (sem as dependências de desenvolvimento)
RUN poetry install --no-dev

# Definindo o diretório de trabalho para /app
WORKDIR /app

# Copiando o código-fonte da aplicação para o contêiner
COPY . /app/

# Expondo a porta 8000 para acesso ao servidor
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

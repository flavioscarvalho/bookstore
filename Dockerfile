# Estágio base com dependências do sistema e Python
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
    VENV_PATH="/opt/pysetup/.venv" \
    POETRY_CACHE_DIR="/var/cache/poetry"

# Adicionando Poetry e venv ao PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instalando dependências do sistema e do Python
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev \
        python3-dev \
        bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalando o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Configurando o diretório de trabalho e copiando os arquivos de requisitos do projeto
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Instalando as dependências do projeto (sem as dependências de desenvolvimento)
RUN poetry install --no-dev

# Estágio final para executar a aplicação com um ambiente mais limpo
FROM python:3.12.2-slim

# Definindo variáveis de ambiente para Python, pip e Poetry
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    VENV_PATH="/opt/pysetup/.venv"

# Adicionando venv ao PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Instalando bash no estágio final
RUN apt-get update && \
    apt-get install --no-install-recommends -y bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiando apenas os arquivos necessários para o estágio final
COPY --from=python-base $POETRY_HOME $POETRY_HOME
COPY --from=python-base $VENV_PATH $VENV_PATH
COPY --from=python-base /opt/pysetup /opt/pysetup

# Definindo o diretório de trabalho para /app
WORKDIR /app

# Copiando o código-fonte da aplicação para o contêiner
COPY . /app/

# Expondo a porta 8000 para acesso ao servidor
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

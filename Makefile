# Versão do Python usada no projeto
PYTHON_VERSION ?= 3.8.10

# Diretórios que contêm os módulos da biblioteca que este repositório compila
LIBRARY_DIRS = order product bookstore

# Diretório de build
BUILD_DIR ?= build

# Opções do PyTest
PYTEST_HTML_OPTIONS = --html=$(BUILD_DIR)/report.html --self-contained-html
PYTEST_TAP_OPTIONS = --tap-combined --tap-outdir $(BUILD_DIR)
PYTEST_COVERAGE_OPTIONS = --cov=$(LIBRARY_DIRS)
PYTEST_OPTIONS ?= $(PYTEST_HTML_OPTIONS) $(PYTEST_TAP_OPTIONS) $(PYTEST_COVERAGE_OPTIONS)

# Opções do MyPy para checagem de tipos
MYPY_OPTS ?= --python-version $(basename $(PYTHON_VERSION)) --show-column-numbers --pretty --html-report $(BUILD_DIR)/mypy

# Caminhos para instalação do Python
PYTHON_VERSION_FILE = .python-version
ifeq ($(shell which pyenv),)
    PYENV_VERSION_DIR ?= $(HOME)/.pyenv/versions/$(PYTHON_VERSION)
else
    PYENV_VERSION_DIR ?= $(shell pyenv root)/versions/$(PYTHON_VERSION)
endif
PIP ?= pip3

POETRY_OPTS ?=
POETRY ?= poetry $(POETRY_OPTS)
RUN_PYPKG_BIN = $(POETRY) run

# Cores para a saída no terminal
COLOR_ORANGE = \033[33m
COLOR_RESET = \033[0m

##@ Utility

.PHONY: help
help:  ## Exibe esta ajuda
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: version-python
version-python: ## Exibe a versão do Python em uso
	@echo $(PYTHON_VERSION)

##@ Testes

.PHONY: test
test: ## Executa os testes
	$(RUN_PYPKG_BIN) pytest $(PYTEST_OPTIONS) tests/*.py

##@ Build e Publicação

.PHONY: build
build: ## Executa o build
	$(POETRY) build

.PHONY: publish
publish: ## Publica o build no repositório configurado
	$(POETRY) publish $(POETRY_PUBLISH_OPTIONS_SET_BY_CI_ENV)

.PHONY: deps-py-update
deps-py-update: pyproject.toml ## Atualiza dependências do Poetry
	$(POETRY) update

##@ Setup

.PHONY: deps
deps: deps-brew deps-py  ## Instala todas as dependências

.PHONY: deps-brew
deps-brew: Brewfile ## Instala dependências de desenvolvimento via Homebrew
	brew bundle --file=Brewfile
	@echo "$(COLOR_ORANGE)Certifique-se de que o pyenv está configurado no seu shell.$(COLOR_RESET)"
	@echo "$(COLOR_ORANGE)Ele deve ter algo como 'eval \$$(pyenv init -)'$(COLOR_RESET)"

.PHONY: deps-py
deps-py: $(PYTHON_VERSION_FILE) ## Instala dependências do Python
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade poetry
	$(POETRY) install

##@ Qualidade de Código

.PHONY: check
check: check-py ## Executa linters e outras verificações

.PHONY: check-py
check-py: check-py-flake8 check-py-black check-py-mypy ## Verifica arquivos Python

.PHONY: check-py-flake8
check-py-flake8: ## Executa o linter flake8
	$(RUN_PYPKG_BIN) flake8 --exclude=venv .

.PHONY: check-py-black
check-py-black: ## Verifica formatação com o black
	-$(RUN_PYPKG_BIN) black --check --line-length 118 --fast .

.PHONY: check-py-mypy
check-py-mypy: ## Executa o mypy para checagem de tipos
	$(RUN_PYPKG_BIN) mypy $(MYPY_OPTS) $(LIBRARY_DIRS)

##@ Formatação de Código

.PHONY: format-py
format-py: ## Formata o código com black
	$(RUN_PYPKG_BIN) black .

.PHONY: format-autopep8
format-autopep8: ## Formata o código com autopep8
	$(RUN_PYPKG_BIN) autopep8 --in-place --recursive .

.PHONY: format-isort
format-isort: ## Organiza imports com isort
	$(RUN_PYPKG_BIN) isort .

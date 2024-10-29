# Bookstore

A comprehensive API for managing book collections, orders, and categories, developed as part of the Backend Python course from EBAC.

## Prerequisites

- **Python 3.12.2** - [Installation Guide](https://www.python.org/downloads/)
- **Poetry 1.8.4** - [Installation Guide](https://python-poetry.org/docs/#installation)
- **Docker & Docker-Compose** - [Docker Installation Guide](https://docs.docker.com/get-docker/)

## Quickstart in One Terminal

```shell
# Clone the project and navigate to its directory
git clone https://github.com/flavioscarvalho/bookstore.git && cd bookstore

# Install dependencies with Poetry
poetry install

# Run migrations and start the local development server
poetry run python manage.py migrate && poetry run python manage.py runserver

# Build and start the Docker environment, then run migrations
docker-compose up -d --build && docker-compose exec web python manage.py migrate

# Run tests inside the Docker environment
docker-compose exec web python manage.py test

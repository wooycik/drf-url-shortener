# drf-url-shortener
Django Rest Framework app for shortening URLs

## Installation
You can run this project using Docker.

### Build the Docker image
```sh
docker build -t drf-url-shortener .
```

### Run the Docker container
```sh
docker run -p 8000:8000 drf-url-shortener
```

The app will be available at http://localhost:8000.

### Generate migrations
```sh
docker run --rm -v $(pwd):/app drf-url-shortener python manage.py makemigrations
```

### Running migrations
```sh
docker run --rm drf-url-shortener python manage.py migrate
```

### Running black formatter
```sh
docker run --rm drf-url-shortener black .
```

### Running ruff linter
```sh
docker run --rm drf-url-shortener ruff check .
```

### Running tests with pytest
```sh
docker run --rm drf-url-shortener pytest
```
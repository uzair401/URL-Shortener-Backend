# URL Shortener Backend

This project is a Django-based URL Shortener API that allows users to shorten URLs, retrieve the original URLs, update or delete shortened URLs, and view statistics for each shortened URL. This is a home takeaway assignment project by Innovaxel.

## Deployed Link
```bash
https://url-shortener-1ic7.onrender.com/swagger
```
## Features

- **Shorten URL**: Generate a short URL for a given original URL.
- **Redirect URL**: Retrieve the original URL using the short URL.
- **Update URL**: Update the original URL associated with a short URL.
- **Delete URL**: Delete a short URL.
- **Statistics**: View statistics such as hit count for a short URL.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Collect static files:
    ```bash
    python manage.py collectstatic --noinput
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### 1. Shorten URL
- **Endpoint**: `/shorten/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
     "original_url": "https://example.com"
  }
  ```
- **Response**:
  ```json
  {
     "short_url": "abc123",
     "original_url": "https://example.com",
     "created_at": "2025-04-19T15:23:00Z",
     "updated_at": "2025-04-19T15:23:00Z",
     "hit_count": 0
  }
  ```

### 2. Redirect URL
- **Endpoint**: `/<short_url>/`
- **Method**: `GET`
- **Response**:
  ```json
  {
     "short_url": "abc123",
     "original_url": "https://example.com",
     "hit_count": 1
  }
  ```

### 3. Update URL
- **Endpoint**: `/update/<short_url>/`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
     "original_url": "https://new-example.com"
  }
  ```
- **Response**:
  ```json
  {
     "short_url": "abc123",
     "original_url": "https://new-example.com",
     "updated_at": "2025-04-20T10:00:00Z"
  }
  ```

### 4. Delete URL
- **Endpoint**: `/delete/<short_url>/`
- **Method**: `DELETE`
- **Response**: `204 No Content`

### 5. Statistics
- **Endpoint**: `/statistics/<short_url>/`
- **Method**: `GET`
- **Response**:
  ```json
  {
     "short_url": "abc123",
     "original_url": "https://example.com",
     "hit_count": 10
  }
  ```

## Middleware and Libraries

- **Gunicorn**: Used as the WSGI HTTP server.
- **WhiteNoise**: Serves static files efficiently.
- **Django CORS Headers**: Handles Cross-Origin Resource Sharing (CORS).

## Development

### Running Tests
To run tests, use:
```bash
python manage.py test
```

### Code Structure
- **`main_app/models.py`**: Contains the `ShortURL` model.
- **`main_app/views.py`**: Contains API views for URL shortening, redirection, updating, deletion, and statistics.
- **`main_app/serializers.py`**: Serializes and deserializes data for the `ShortURL` model.
- **`main_app/urls.py`**: Defines API endpoints.
- **`url_shortener_API/settings.py`**: Configures Django settings, including CORS and static file handling.

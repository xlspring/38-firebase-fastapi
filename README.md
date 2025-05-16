# FastAPI Demo Application

A simple RESTful API built with FastAPI.

## Features

- CRUD operations for items
- RESTful API design
- In-memory database for demo purposes
- Automated testing with pytest
- Containerization with Docker
- CI/CD with GitHub Actions
- Firebase hosting setup

## Getting Started

### Local Development

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

3. Access the API documentation:
   ```
   http://localhost:8000/docs
   ```

### Running Tests

```
pytest app/tests
```

### Docker

1. Build the Docker image:
   ```
   docker build -t fastapi-demo .
   ```

2. Run the container:
   ```
   docker run -p 8000:8000 fastapi-demo
   ```

## Deployment

### GitHub Actions

The application uses GitHub Actions for CI/CD:
1. Runs tests on every push to main branch
2. Builds and pushes Docker image to GitHub Container Registry
3. Deploys the application to Firebase hosting

Required secrets in your GitHub repository:
- `FIREBASE_PROJECT_ID`: Your Firebase project ID
- `FIREBASE_TOKEN`: Firebase CLI authentication token

To get your Firebase token:
```
firebase login:ci
```

## API Endpoints

- `GET /`: Welcome message
- `GET /items`: Get all items
- `GET /items/{item_id}`: Get a specific item
- `POST /items`: Create a new item
- `DELETE /items/{item_id}`: Delete an item 
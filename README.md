# Todo App with CI/CD

A simple todo application with Flask, MySQL, Nginx, and GitHub Actions CI/CD.

## Setup instructions

```bash
# Clone and start with Docker Compose
git clone this_repo
cd todo-app-ci
docker-compose up --build
```

The app will be available at `http://localhost`

## Project Structure

```
.
├── web/                # Flask app, tests
├── nginx/              # Reverse proxy config
├── db/                 # Database schema
├── docker-compose.yml  # Multi-container setup
└── .github/workflows/  # CI/CD pipelines
```

## API Endpoints

- `GET /health` - Health check
- `GET /` - Web interface
- `POST /add` - Add task (JSON): `{"task": "..."}`
- `GET /list` - Get all tasks
- `GET /delete/<id>` - Delete task
- `POST /add_from_browser` - Add via form

## CI/CD Pipelines

**Python Application** (`python-app.yml`)
- Black formatting check
- flake8 linting
- pytest >80% code coverage
- Triggered on push/PR to main

**Docker Image** (`docker-image.yml`)
- Dockerfile validation
- Docker build and test
- Triggered on push/PR to main (when Dockerfile changes)

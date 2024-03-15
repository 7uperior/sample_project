# Sample Hexagonal Architecture PythonProject
## Setup, Development, and Testing Guide

[![codecov](https://codecov.io/gh/7uperior/sample_project/branch/main/graph/badge.svg?token=e8020596-f3f4-4cb8-8146-d37df105f70b)](https://codecov.io/gh/7uperior/sample_project)


This guide outlines the setup, development, and testing processes for the Sample Project, a Python RESTful application implementing the Hexagonal Architecture pattern. It leverages FastAPI and SQLAlchemy for the backend, and is containerized using Docker for easy development and deployment.

### Prerequisites

Before starting, ensure you have the following tools installed:

- Docker
- Docker Compose
- Poetry (Python package manager)

### Release Notes

- Ensure compatibility with SQLAlchemy versions below 2.0
- Ensure compatibility with Pydantic versions below 2.0
- Development is managed using Poetry. Docker containers are built using `requirements.txt`. Use the following command to update `requirements.txt` for Docker images as needed: `poetry export -f requirements.txt --output requirements.txt --without-hashes`

### Setup Instructions

1. **Clone the Repository**: Clone this project to your local machine.

2. **Environment Variables**: Copy `.env.example` to `.env` and modify as necessary. This file includes important configurations, such as database connection details.

3. **Synchronize Dependencies**: Run `poetry export -f requirements.txt --output requirements.txt --without-hashes` to ensure `requirements.txt` is up-to-date with project dependencies, excluding hashes.

4. **Start the Development Environment**: Launch the development environment with Docker Compose by running `docker-compose up --build`.

### Testing

Execute the built-in unit tests by running `pytest` in the project's root directory.

### Updating Packages

To update project dependencies and synchronize the Docker environment:

1. Update dependencies with `poetry update`.
2. Export the updated dependencies to `requirements.txt` using `poetry export -f requirements.txt --output requirements.txt --without-hashes`.
3. Rebuild and start the Docker environment with `docker-compose up --build` to apply the updates.


## Author

- [@7uperior](https://github.com/7uperior)
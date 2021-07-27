# TOFU BACKEND

## Requirements

- Docker
- Docker Compose
- Python 3

## Running on local machine

Build the base dockers:
```bash
make build-base
```

Run docker compose:
```bash
docker-compose up
```

To run again after modifications:
```bash
docker-compose up --build
```
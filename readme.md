# Budget App
This is a simple example application built in Python on Flask framework. Served up on a Docker container with gunicorn and has it's data stored in PostGres.

## Installation
Use pip to install the required dependencies from the `requirements.txt` file.

```
pip install .
```

## Running on Docker
If you want to run this whole setup in Docker simply run `docker-compose up`. This will build the application with the latest PostGres image and the `python:3.9` image.

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
d5f2785e6ea1        budget_budget-api   "gunicorn --config c…"   4 hours ago         Up 4 hours          0.0.0.0:5000->5000/tcp   budget-api
836bce9cbb1e        postgres            "docker-entrypoint.s…"   2 days ago          Up 4 hours          0.0.0.0:5432->5432/tcp   budget-db
```

## Testing
The application uses PyTest. Which means your test suite is as easy as `pytest tests`.
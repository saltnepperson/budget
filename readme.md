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
CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS              PORTS                                                                NAMES
68328d96b3d1        budget_budget-api       "gunicorn --config c…"   About an hour ago   Up About an hour    0.0.0.0:5000->5000/tcp                                               budget-api
fa7216b96f9e        localstack/localstack   "docker-entrypoint.sh"   About an hour ago   Up About an hour    0.0.0.0:4566-4599->4566-4599/tcp, 0.0.0.0:8081->8081/tcp, 8080/tcp   localstack
836bce9cbb1e        postgres                "docker-entrypoint.s…"   6 days ago          Up About an hour    0.0.0.0:5432->5432/tcp                                               budget-db
```

## Testing
The application uses PyTest. Which means your test suite is as easy as `pytest tests`.

## LocalStack
The application currently relies on [localstack](https://github.com/localstack/localstack). It's included in the `docker-compose.yml` file for this repository. **Note**: if you are on Mac OS you will need to execute the following command with the `docker-compose` command: `TMPDIR=/private$TMPDIR docker-compose up`.

With that infrastructure in place you can test your local Kinesis instance by running the command `aws --profile <profile-name-here> --endpoint-url=http://localhost:4566 kinesis list-streams`. **Note on testing** because the URL for the Kinesis instance is hardcoded in the `/budget/tests/feature/test_kinesis_connection.py` test, if this value is different for you, be sure to change it there.
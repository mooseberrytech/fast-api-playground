# FastAPI Playground

This is a repository for trying out [FastAPI](https://fastapi.tiangolo.com/) with various libraries.

## How to install

The project is using [poetry](https://python-poetry.org/) for managing dependencies. 

`poetry install`

## How to run the app

`poetry run fastapi dev src/main.py`

## How to run the schemathesis tests

1. Run the app 
2. Run `poetry run st run http://127.0.0.1:8000/openapi.json --experimental=openapi-3.1  -c all`



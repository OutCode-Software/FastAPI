# FastAPI Package Creator

This is a simple FastAPI application for creating and retrieving package data. The application exposes two endpoints:

- /: A simple root endpoint that returns a greeting message.
- /package/: An endpoint that accepts an HTTP POST request with package data in the request body, validates it using Pydantic models, and returns the parsed data as a JSON response.

## Requirements

To run this application, you will need:

- Python 3.7 or later
- pip (Python package manager)
- A terminal or command prompt

## Installation

To install the required packages, run the following command:

```bash
pip install fastapi uvicorn[standard] pydantic
```

This will install the FastAPI and Pydantic packages, as well as the uvicorn server, which we will use to run the application.

## Usage

To run the application, navigate to the root directory of the project and run the following command:

```bash
uvicorn main:app --reload
```

This will start the application server and enable auto-reloading of the code when changes are made.

You can now access the application endpoints by navigating to <http://localhost:8000/> and <http://localhost:8000/package/> in your web browser or using a tool like curl or httpie.

## API Reference

The application exposes the following endpoints:

\``GET /`\`

A simple root endpoint that returns a greeting message.

`Example Request`

```bash
http GET http://localhost:8000/
```

`Example Response`

```json
{
    "Hello": "World"
}
```

\``POST /package/`\`

An endpoint that accepts an HTTP POST request with package data in the request body, validates it using Pydantic models, and returns the parsed data as a JSON response.

`Request Body`

The request body must be a JSON object with the following fields:

- `secret_id` (integer, required): A unique identifier for the package.
- `name` (string, required): The name of the package.
- `number` (string, required): The package tracking number.
- `description` (string, optional): A description of the package.

`Response Body`

The response body will be a JSON object with the following fields:

- `name` (string): The name of the package.
- `number` (string): The package tracking number.
- `description` (string, optional): A description of the package.

`Example Request`

```bash
$ http POST <http://localhost:8000/package/> secret_id=123 name='FastAPI' number='123456' description='A web framework for building APIs'
```

`Example Response`

```json
{
    "name": "FastAPI",
    "number": "123456",
    "description": "A web framework for building APIs"
}
```

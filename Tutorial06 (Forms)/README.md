# FastAPI Language Endpoint Example

This is a simple example of a FastAPI endpoint that expects two parameters, "name" and "type", both of type string, sent as form data via a POST request to the "/language/" endpoint. The endpoint returns a dictionary containing the received parameters.

## Installation

To install the necessary dependencies, run:

```bash
pip install fastapi uvicorn
```

## Usage

To start the server, run:

```bash
uvicorn main:app --reload
```

Then, navigate to `http://localhost:8000/docs` in your web browser to access the Swagger UI, where you can try out the /language/ endpoint by submitting a form with "name" and "type" fields.

Alternatively, you can use a tool like cURL or Postman to send a POST request to `http://localhost:8000/language/` with form data containing "name" and "type" fields.

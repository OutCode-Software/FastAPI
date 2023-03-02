# Package Maker API

This is a simple API for creating packages with a given priority.

## Requirements

To run this API, you'll need:

- Python 3.6 or later
- FastAPI and its dependencies
- Pydantic and its dependencies

## Usage

\``GET /`\`

This endpoint returns a simple "Hello, World!" message:

```bash
$ http GET http://localhost:8000/
HTTP/1.1 200 OK
content-length: 17
content-type: application/json
date: Sat, 27 Feb 2023 00:00:00 GMT

{
    "Hello": "World"
}
```

\``POST /package/{priority}`\`

This endpoint creates a package with the given priority and data.

The priority is passed as a URL parameter, the package data is passed in the request body as JSON, and a boolean value is passed in the query string.

Example request:

```bash
$ http POST http://localhost:8000/package/42 value:=true name=foo number=1234 description=bar
HTTP/1.1 200 OK
content-length: 70
content-type: application/json
date: Sat, 27 Feb 2023 00:00:00 GMT

{
    "description": "bar",
    "name": "foo",
    "number": "1234",
    "priority": 42,
    "value": true
}
```

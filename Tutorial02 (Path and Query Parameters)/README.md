# FastAPI Sample Project

This is a simple FastAPI project that demonstrates how to define routes with different types of parameters (path parameters and query parameters) and return JSON responses.

## Requirements

To run this project, you need to have Python 3.6 or later installed on your system.

You also need to install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload
```

This will start the application on http://localhost:8000.

## Endpoints

This project defines the following endpoints:

\``/`\`

Returns a simple JSON message.

Example:

```bash
$ curl http://localhost:8000/
{"Hello":"World"}
```

\`/component/{component_id}\`

Accepts a path parameter component_id and returns a JSON message containing the value of the parameter.

Example:

```bash
$ curl http://localhost:8000/component/123
{"component_id":123}
```

\`/component/\`

Accepts query parameters number (required) and text (optional) and returns a JSON message containing the values of the parameters.

Example:

```bash
$ curl http://localhost:8000/component/?number=42&text=hello
{"number":42,"text":"hello"}
```

# FastAPI Async Endpoint Example

This is an example of a FastAPI endpoint that returns a simple JSON response. The endpoint is defined using the @app.get() decorator, which specifies the URL path and HTTP method to be used. The hello_world() function returns a dictionary with a "Hello" key and "World" value as a JSON response.

## Installation

To run this example, you will need to have Python 3.x installed on your system, as well as the fastapi and uvicorn packages. To install these packages, run the following command:

```bash
pip install fastapi uvicorn
```

## Usage

To run the example, navigate to the directory containing the main.py file and run the following command:

```bash
uvicorn main:app --reload
```

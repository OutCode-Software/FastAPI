# Importing necessary dependencies
from typing import Optional
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a GET endpoint that returns a dictionary with a "Hello" key and "World" value
# The endpoint is defined using the decorator syntax
# The decorator specifies the URL path for the endpoint ("/" in this case) and the HTTP method to be used (GET in this case)
# The function name does not matter, as the decorator determines how the endpoint is accessed
# The function returns the dictionary as a JSON response
@app.get("/")
async def hello_world():
    return {"Hello": "World"}
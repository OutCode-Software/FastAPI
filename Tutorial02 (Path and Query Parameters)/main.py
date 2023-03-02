from typing import Optional # import Optional type hint for optional parameters
from fastapi import FastAPI # import the FastAPI class from the fastapi module

# create a new instance of the FastAPI class
app = FastAPI()

# define a route for the root path ("/") that returns a simple JSON message
@app.get("/")
async def hello_world():
    return {"Hello": "World"}

# define a route for the "/component/{component_id}" path that accepts a path parameter "component_id"
@app.get("/component/{component_id}") # curly braces indicate a path parameter
async def get_component(component_id: int):
    return {"component_id": component_id}

# define a route for the "/component/" path that accepts query parameters "number" and "text"
@app.get("/component/")
async def read_component(number: int, text: Optional[str]): # Optional indicates that "text" parameter is optional
    return {"number": number, "text": text}

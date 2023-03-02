from typing import Optional  # Import Optional to allow for optional fields in Pydantic models
from fastapi import FastAPI  # Import FastAPI framework
from pydantic import BaseModel  # Import Pydantic BaseModel to define data models

# Define a Pydantic model for the package data
class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None  # Allow for an optional description field

# Create a FastAPI instance
app = FastAPI()

# Define a route for the root URL
@app.get("/")
async def hello_world():
    return {"Hello": "World"}

# Define a route for creating a package with a given priority
# The priority is passed as a URL parameter, the package data is passed in the request body, and a boolean value is passed in the query string
@app.post("/package/{priority}")
async def make_package(priority: int, package: Package, value: bool):
    # Return a dictionary containing the priority, package data, and boolean value
    return {"priority": priority, **package.dict(), "value": value}

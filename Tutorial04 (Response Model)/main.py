from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Define a Pydantic model for the incoming package data
class PackageIn(BaseModel):
    secret_id: int
    name: str
    number: str
    description: Optional[str] = None

# Define a Pydantic model for the outgoing package data
class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None

# Create a FastAPI instance
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
async def hello_world():
    # Return a JSON response with a simple greeting
    return {"Hello": "World"}

# Define a route for creating a new package
@app.post("/package/", response_model=Package, response_model_include={"description"})
async def make_package(package: PackageIn):
    # Return the incoming package data as a JSON response
    return package

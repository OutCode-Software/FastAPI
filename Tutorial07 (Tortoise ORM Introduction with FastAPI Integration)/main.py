# Import required modules
from fastapi import FastAPI, HTTPException
from models import Todo, TodoIn_Pydantic, Todo_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from pydantic import BaseModel

# Define a new Message Pydantic model class with a single field named "message"
class Message(BaseModel):
    message: str

# Create a new FastAPI application instance
app = FastAPI()

# Define a root endpoint that returns a JSON object with a "Hello" key and "World" value
@app.get('/')
async def read_root():
    return {"Hello": "World"}

# Define a "create" endpoint that expects a TodoIn_Pydantic Pydantic model instance in the request body
# This endpoint creates a new Todo object in the database and returns a JSON response with a Todo_Pydantic Pydantic model instance
@app.post('/todo', response_model=Todo_Pydantic)
async def create(todo: TodoIn_Pydantic):
    obj = await Todo.create(**todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_tortoise_orm(obj)

# Define a "get_one" endpoint that expects an "id" integer parameter and returns a JSON response with a Todo_Pydantic Pydantic model instance
# If the requested Todo object is not found, this endpoint raises an HTTPNotFoundError exception with a JSON response
@app.get('/todo/{id}', response_model=Todo_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_one(id: int):
    return await Todo_Pydantic.from_queryset_single(Todo.get(id=id))

# Define an "update" endpoint that expects an "id" integer parameter and a TodoIn_Pydantic Pydantic model instance in the request body
# This endpoint updates an existing Todo object in the database and returns a JSON response with a Todo_Pydantic Pydantic model instance
# If the requested Todo object is not found, this endpoint raises an HTTPNotFoundError exception with a JSON response
@app.put("/todo/{id}", response_model=Todo_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update(id: int, todo: TodoIn_Pydantic):
    await Todo.filter(id=id).update(**todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_queryset_single(Todo.get(id=id))

# Define a "delete" endpoint that expects an "id" integer parameter and deletes the corresponding Todo object from the database
# If the requested Todo object is not found, this endpoint raises an HTTPNotFoundError exception with a JSON response
@app.delete("/todo/{id}", response_model=Message, responses={404: {"model": HTTPNotFoundError}})
async def delete(id: int):
    delete_obj = await Todo.filter(id=id).delete()
    if not delete_obj:
        raise HTTPException(status_code=404, detail="This todo is not found.")
    return Message(message="Succesfully Deleted")

# Use the register_tortoise function from Tortoise's FastAPI module to register the Tortoise ORM with the FastAPI app
# This creates a connection to the database and generates the database schema based on the defined models
# It also adds exception handlers for Tortoise-specific exceptions to return appropriate JSON responses
register_tortoise(
    app,
    db_url="sqlite://store.db", # Specify the database URL
    modules={'models': ['models']}, # Specify the location of the model classes
    generate_schemas=True, # Generate the database schema automatically
    add_exception_handlers=True, # Add exception handlers for Tortoise-specific exceptions
)
``

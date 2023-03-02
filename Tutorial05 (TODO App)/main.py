# Import required modules
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Define the data model for a Todo item
class Todo(BaseModel):
    name: str
    due_date: str
    description: str

# Create a FastAPI application instance
app = FastAPI(title="Todo API")

# Initialize an empty list to store Todo items
store_todo = []

# Define the route for the home page
@app.get('/')
async def home():
    return {"Hello": "World"}

# Define the route for creating a new Todo item
@app.post('/todo/')
async def create_todo(todo: Todo):
    # Add the new Todo item to the list
    store_todo.append(todo)
    # Return the newly created Todo item
    return todo

# Define the route for getting all Todo items
@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    # Return the list of all Todo items
    return store_todo

# Define the route for getting a single Todo item by ID
@app.get('/todo/{id}')
async def get_todo(id: int):
    try:
        # Return the Todo item with the specified ID
        return store_todo[id]
    except:
        # If the Todo item is not found, raise an HTTPException with a 404 status code
        raise HTTPException(status_code=404, detail="Todo Not Found")

# Define the route for updating a Todo item by ID
@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):
    try:
        # Update the Todo item with the specified ID with the new data
        store_todo[id] = todo
        # Return the updated Todo item
        return store_todo[id]
    except:
        # If the Todo item is not found, raise an HTTPException with a 404 status code
        raise HTTPException(status_code=404, detail="Todo Not Found")

# Define the route for deleting a Todo item by ID
@app.delete('/todo/{id}')
async def delete_todo(id: int):
    try:
        # Get the Todo item with the specified ID
        obj = store_todo[id]
        # Remove the Todo item from the list
        store_todo.pop(id)
        # Return the deleted Todo item
        return obj
    except:
        # If the Todo item is not found, raise an HTTPException with a 404 status code
        raise HTTPException(status_code=404, detail="Todo Not Found")

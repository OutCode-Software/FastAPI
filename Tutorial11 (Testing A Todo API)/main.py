from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Define the data model for a todo item using Pydantic's BaseModel
class Todo(BaseModel):
    name: str
    due_date: str
    description: str

# Initialize a new FastAPI instance with the title "Todo API"
app = FastAPI(title="Todo API")

# Create an empty list to store all the todos
store_todo = []

# Define the route for the homepage, returning a simple "Hello World" message
@app.get('/')
async def home():
    return {"Hello": "World"}

# Define the route for creating a new todo item
@app.post('/todo/')
async def create_todo(todo: Todo):
    # Append the new todo to the list of todos and return it
    store_todo.append(todo)
    return todo

# Define the route for retrieving all todo items
@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    return store_todo

# Define the route for retrieving a specific todo item by its ID
@app.get('/todo/{id}')
async def get_todo(id: int):
    try:
        # Attempt to return the todo with the given ID
        return store_todo[id]
    except:
        # If the ID is invalid, raise an HTTPException with a 404 status code and a "Todo Not Found" message
        raise HTTPException(status_code=404, detail="Todo Not Found")
    
# Define the route for updating a specific todo item by its ID
@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):
    try:
        # Attempt to update the todo with the given ID and return the updated todo
        store_todo[id] = todo
        return store_todo[id]
    except:
        # If the ID is invalid, raise an HTTPException with a 404 status code and a "Todo Not Found" message
        raise HTTPException(status_code=404, detail="Todo Not Found")
    
# Define the route for deleting a specific todo item by its ID
@app.delete('/todo/{id}')
async def delete_todo(id: int):
    try:
        # Attempt to remove the todo with the given ID from the list of todos and return it
        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    except:
        # If the ID is invalid, raise an HTTPException with a 404 status code and a "Todo Not Found" message
        raise HTTPException(status_code=404, detail="Todo Not Found")

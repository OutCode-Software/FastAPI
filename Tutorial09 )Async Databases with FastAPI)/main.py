from typing import List

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
import databases
import sqlalchemy
from datetime import datetime

# The database URL where our SQLite database will be created
DATABASE_URL = "sqlite:///./store.db"

# Define metadata for SQLAlchemy to create tables
metadata = sqlalchemy.MetaData()

# Create a Database instance using the DATABASE_URL
database = databases.Database(DATABASE_URL)

# Define a table to store user data
register = sqlalchemy.Table(
    "register",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(500)),
    sqlalchemy.Column("date_created", sqlalchemy.DateTime())
)

# Create an engine to connect to our database
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create the table in our database if it doesn't already exist
metadata.create_all(engine)

# Create a FastAPI instance
app = FastAPI()

# Connect to the database when the app starts up
@app.on_event("startup")
async def connect():
    await database.connect()

# Disconnect from the database when the app shuts down
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Define a Pydantic model for creating a new user
class RegisterIn(BaseModel):
    name: str = Field(...)

# Define a Pydantic model for returning user data
class Register(BaseModel):
    id: int
    name: str
    date_created: datetime 

# Create a route for creating a new user
@app.post('/register/', response_model=Register)
async def create(r: RegisterIn = Depends()):
    # Insert the new user's data into the register table
    query = register.insert().values(
        name=r.name,
        date_created=datetime.utcnow()
    )
    # Get the ID of the new user record
    record_id = await database.execute(query)
    # Retrieve the new user record from the register table
    query = register.select().where(register.c.id == record_id)
    row = await database.fetch_one(query)
    # Return the new user record as a Register object
    return {**row}

# Create a route for retrieving a single user by ID
@app.get('/register/{id}', response_model=Register)
async def get_one(id: int):
    # Retrieve the user record with the specified ID
    query = register.select().where(register.c.id == id)
    user = await database.fetch_one(query)
    # Return the user record as a Register object
    return {**user}

# Create a route for retrieving all user records
@app.get('/register/', response_model=List[Register])
async def get_all():
    # Retrieve all user records from the register table
    query = register.select()
    all_get = await database.fetch_all(query)
    # Return all user records as a list of Register objects
    return all_get

# Create a route for updating an existing user record
@app.put('/register/{id}', response_model=Register)
async def update(id: int, r: RegisterIn = Depends()):
    # Update the user record with the specified ID
    query = register.update().where(register.c.id == id).values(
        name=r.name,
        date_created=datetime.utcnow(),
    )
    # Retrieve the updated user record from the register table
    record_id = await database.execute(query)
    query = register.select().where(register.c.id == record_id)
    row = await database.fetch_one(query)
    # Return the updated user record as a Register object
    return {**row}

# Define a route to delete a record from the "register" table in the database
@app.delete("/register/{id}", response_model=Register)
async def delete(id: int):
    # Create a delete query to remove the record with the matching ID from the "register" table
    query = delete().where(register.c.id == id)
    # Execute the delete query on the database
    result = await database.execute(query)
    # Return the deleted record as a response
    return result

from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
# def hello_world():
#     return {"Hello": "World"}
async def hello_world():
    return {"Hello": "World"}
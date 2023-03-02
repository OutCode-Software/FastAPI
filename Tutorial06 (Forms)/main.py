# Import the FastAPI library
from fastapi import FastAPI, Form

# Create a new FastAPI application instance
app = FastAPI()

# Define a POST endpoint at /language/
@app.post('/language/')
async def language(name: str = Form(...), type: str = Form(...)):
    # The endpoint expects two parameters: "name" and "type", both of type string
    # The parameters are decorated with the Form object, indicating they will be received as form data
    # The ... default value is used to indicate that the parameters are required
    return {"name": name, "type": type}
    # Return a dictionary with the received parameters


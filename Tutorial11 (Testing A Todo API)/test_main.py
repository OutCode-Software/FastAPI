# Import the TestClient from FastAPI and the main app module
from fastapi.testclient import TestClient
from main import app 

# Create a TestClient instance to test our endpoints
client = TestClient(app)

# Create a dictionary to represent the data of a Todo item
data = {
    "name": "IsaiahT-Tech",
    "due_date": "Today",
    "description": "string"
}

# Test creating a new Todo item
def test_create_todo():
    # Send a POST request to the /todo/ endpoint with the JSON data
    response = client.post("/todo/", json=data)
    
    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check that the response JSON data matches the data we sent
    assert response.json() == data

# Test getting a list of all Todo items
def test_get_all_todo():
    # Send a GET request to the /todo/ endpoint
    response = client.get("/todo/", json=data)
    
    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check that the data we sent is in the response JSON data
    assert data in response.json()

# Test getting a single Todo item by ID
def test_get_todo():
    # Send a GET request to the /todo/ endpoint with the ID of 0
    response = client.get("/todo/0")
    
    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check that the response JSON data matches the data we sent
    assert response.json() == data

# Test updating a single Todo item by ID
def test_update_todo():
    # Send a PUT request to the /todo/ endpoint with the ID of 0 and new data
    response = client.put("/todo/0", json={
        "name": "Test",
        "due_date": "Now",
        "description": "Python"
    })
    
    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check that the response JSON data matches the new data we sent
    assert response.json() == {   
        "name": "Test",
        "due_date": "Now",
        "description": "Python"
    }

# Test deleting a single Todo item by ID
def test_delete_todo():
    # Send a DELETE request to the /todo/ endpoint with the ID of 0
    response = client.delete("/todo/0")
    
    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check that the response JSON data matches the data we sent
    assert response.json() == {   
        "name": "Test",
        "due_date": "Now",
        "description": "Python"
    }

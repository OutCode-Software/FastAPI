# Get Start with FastAPI

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## 1. Installation

- Run command on your terminal/command prompt.

    ```bash
        pip install fastapi
        pip install uvicorn
    ```

## Description

- Pydantic is a Python library for data validation and settings management using Python type annotations. It is used by FastAPI to validate incoming and outgoing data, such as request bodies and query parameters.

- Pydantic uses the Python type hints feature to define the shape and data types of data being validated. For example, the following code defines a Pydantic model for a user with a name and age:

    ```python
    from pydantic import BaseModel

    class User(BaseModel):
        name: str
        age: int
    ```

- Pydantic automatically validates incoming data against the defined model, checking if the data is of the correct type, if required fields are present, and if values conform to any additional constraints specified in the model.

- In addition to data validation, Pydantic can also be used for settings management, as it supports loading configuration from a variety of sources such as environment variables, JSON files, and command-line arguments.

- Overall, Pydantic provides a fast and flexible way to validate and manage data in Python, making it a popular choice for building web APIs and other applications.

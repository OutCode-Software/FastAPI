# Import required modules
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

# Define a new Todo model class that extends Tortoise's Model class
class Todo(models.Model):
    
    # Define fields for the Todo model
    # id field with IntField data type, marked as primary key with pk=True
    id = fields.IntField(pk=True)
    # todo field with CharField data type and max length of 250 characters
    todo = fields.CharField(max_length=250)
    # due_date field with CharField data type and max length of 250 characters
    due_date = fields.CharField(max_length=250)
    
    # Define a PydanticMeta subclass within the Todo model class
    # This subclass can be used to define Pydantic model options
    class PydanticMeta:
        pass
    
# Use pydantic_model_creator to generate a Pydantic model based on the Todo model
# The generated model will have the name "Todo" and include all fields from the Todo model
Todo_Pydantic = pydantic_model_creator(Todo, name="Todo")

# Use pydantic_model_creator again to generate a Pydantic model based on the Todo model
# The generated model will have the name "TodoIn" and exclude any readonly fields (which in this case is just the id field)
TodoIn_Pydantic = pydantic_model_creator(Todo, name="TodoIn", exclude_readonly=True)

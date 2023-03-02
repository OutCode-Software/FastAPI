# Todo API

This is a simple API for managing Todo items. The API allows users to create, read, update, and delete Todo items.

## Usage

Once the server is running, you can access the API at http://localhost:8000. The following endpoints are available:

- \``GET /`\` - Returns a "Hello, World!" message.
- \``POST /todo/`\` - Creates a new Todo item.
- \``GET /todo/`\` - Returns a list of all Todo items.
- \``GET /todo/{id}`\` - Returns a single Todo item with the specified ID.
- \``PUT /todo/{id}`\` - Updates a Todo item with the specified ID.
- \``DELETE /todo/{id}`\` - Deletes a Todo item with the specified ID.

All requests and responses use the JSON format. The \``POST /todo/`\` and \``PUT /todo/{id}`\` endpoints expect a JSON object with the following properties:

- \``name`\` - The name of the Todo item (string).
- \``due_date`\` - The due date of the Todo item (string).
- \``description`\` - The description of the Todo item (string).

The \``GET /todo/`\` and \``GET /todo/{id}`\` endpoints return a JSON array or object, respectively, of Todo items with the following properties:

- \``id`\` - The ID of the Todo item (integer).
- \``name`\` - The name of the Todo item (string).
- \``due_date`\` - The due date of the Todo item (string).
- \``description`\` - The description of the Todo item (string).

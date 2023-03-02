from fastapi import FastAPI, Request               # import the FastAPI and Request classes
from fastapi.responses import HTMLResponse         # import the HTMLResponse class
from fastapi.templating import Jinja2Templates     # import the Jinja2Templates class

app = FastAPI()                                    # create a new instance of the FastAPI class

templates = Jinja2Templates(directory="templates") # create a Jinja2Templates instance and specify the directory where the templates are stored

@app.get("/{book}/{id}", response_class=HTMLResponse) # define a route for GET requests with a path parameter for book and id
async def read(request: Request, book: str, id: int): # define a function that handles the request and returns a response
    return templates.TemplateResponse(               # return a response with a rendered HTML template
        "index.html",                                # specify the name of the template to use
        {"request": request, "book": book, "id": id} # provide variables to pass to the template
    )

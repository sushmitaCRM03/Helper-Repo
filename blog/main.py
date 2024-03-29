from typing import Optional
from fastapi import FastAPI
from . import schemas

app = FastAPI()



@app.post('/blog')
def create(request: schemas.Blog):
    #add some random if else statement
    #string manupulation if request.title is a string then convert to uppercase
    #if request.title is a string then convert to uppercase
    return {'data': f'Blog is created with title as {request.title}'}

# dummy test for pr
@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}
# dummy test for pr 2
@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

from typing import Optional
from fastapi import FastAPI
from . import schemas

app = FastAPI()



@app.post('/blog')
def create(request: schemas.Blog):
    return {'data': f'Blog is created with title as {request.title}'}

# dummy test for pr
@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

from typing import Optional
from fastapi import FastAPI
from . import schemas

app = FastAPI()



@app.post('/blog')
def create(request: schemas.Blog):
    return {'data': f'Blog is created with title as {request.title}'}
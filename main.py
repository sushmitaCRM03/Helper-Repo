from fastapi import FastAPI #import FastAPI class
from typing import Optional
from pydantic import BaseModel 
import uvicorn

app = FastAPI() #instance

# how to define this function is actually going to handle a path ::here comes FastAPI will use decorator
@app.get('/') #decorator (this is called as 'path' in FastAPI) not route #get is called as 'operation' and decorator is called as 'path operation decorator '
def name(): #this is called as 'path operation function'
    # this function name can be anything , 
    # function totally doesn't matter what matters 
    # is the decorator 
    # we can name two functions with same name 
    # but we can't have two decorators with same name 
    return {'data': {'name': 'Sushmita'}} #returning a dictionary

@app.get('/about')
def about():
    return {'data': 'about page'}

#path parameters
# we can have multiple path parameters
@app.get('/blog/{id}') #path parameter
def show(id: int): #type hinting
    # fetch blog with id = id
    return {'data': id}

@app.get('blog/unpublished')
def unpublished():
    # fetch unpublished blogs
    return {'data': 'all unpublished blogs'}

#let match first path which is blog a nd then something so when I use blog/unpublished it will match the first path as it is also blog and then it will match the second path
#since int is there it will give error
#so fastapi run one by one and match the path
# so here we can exchange or order of the path, we have to move this type of route before all dynamic routes

@app.get('blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}

#query parameters
@app.get('/blog') #query parameter
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    #http://127.0.0.1:8000/blog?limit=34&published=false
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'} #f string

#mixing path and query parameters
@app.get('/blog/com/{id}')
def show(id: int, limit: int = 10):
    # fetch blog with id = id
    return {'data': {'id': id}}

#request body
#we need to use pydantic model to define the schema of the request body
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog): #request is class object
    return {'data': f'Blog is created with title as {request.title}'}

#debugging in fastapi

#cmd + shift + p
#debug: Restart 
#FastAPI

# if __name__ == '__main__':
#     uvicorn.run(app, host='localhost', port=9001) #this is the way to run the server
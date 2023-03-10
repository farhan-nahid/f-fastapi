from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body


class Post(BaseModel):
    title: str
    content: str
    ratting: Optional[int]
    published: bool = True

app = FastAPI()

post_array = []

def find_post(id):
    for post in post_array:
        if post['id'] == id:
            return post
        else:
            return "Post Not Found"

@app.get("/")
async def root():
    return {"message" : "Hello world!"}


# @app.post('/create-post')
# async def create_post(payload: dict = Body(...)):
#     return payload

@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_post(post:Post):
    new_post = post.dict()
    new_post['id'] = len(post_array) + 1
    post_array.append(new_post)
    return new_post



@app.get("/posts")
async def get_post():
    return {"data" : post_array}



@app.get("/posts/latest")
async def get_post():
    if(len(post_array) == 0):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There is no post in the list")
    post = post_array[len(post_array)-1]
    return {"data": post}



@app.get("/posts/{id}")
async def get_single_post(id:int):
    post = find_post(id)
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    return {"data" : post}
from typing import Optional

from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.params import Body


class Post(BaseModel):
    title: str
    content: str
    ratting: Optional[int]
    published: bool = True

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello world!"}


# @app.post('/create-post')
# async def create_post(payload: dict = Body(...)):
#     return payload

@app.post('/create-post')
async def create_post(post:Post):
    return post.dict()

@app.get("/posts")
async def get_post():
    return {"data":"This is all post"}
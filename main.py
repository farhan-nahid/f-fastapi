from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello world!"}


@app.post('/create-post')
async def create_post(payload: dict = Body(...)):
    return payload

@app.get("/posts")
async def get_post():
    return {"data":"This is all post"}
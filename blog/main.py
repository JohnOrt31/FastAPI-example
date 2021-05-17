from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from . import schemas

app = FastAPI()

@app.post('/blog')
def create(request: schemas.Blog):
    return request
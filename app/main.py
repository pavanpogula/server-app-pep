# from aws.aws_controller import get_items_all
import sys,os
sys.path.append(os.path.dirname(sys.path[0]))


from app.aws.aws_controller import get_items_all
from typing import Union
import os
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "UserNotYesNo"}


# @app.get("/get_all")
# def get_items():
    
#     return jsonable_encoder(get_items_all())

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
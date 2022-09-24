from typing import Union
from fastapi import FastAPI, Header, Response, status
from pydantic import BaseModel

import os
from dotenv import load_dotenv

import app.index as index
import app.web as web


load_dotenv()

app = FastAPI()

@app.get("/")
def indexHandler():
    return index.handler()


@app.get("/web/{webPath:path}")
def webHandler(webPath: str, response: Response):
    return web.handler(webPath, response)




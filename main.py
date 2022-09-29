from fastapi import FastAPI, Cookie
from pydantic import BaseModel
from typing import Union

import app.pre_register as pre_register
import app.register as register
import app.login as login


import app.profile as profile
import app.chat as chat
import app.conversation as conversation
import app.history as history

# 環境変数を共有
import app.global_var as g

# アプリケーションオブジェクトインスタンスの生成
app = FastAPI()

@app.post("/api/login")
def LoginHandler(cookie: Union[str, None] = Cookie(default=None)):
	return {"a", "b"}


class pre_registerStruct(BaseModel):
	mail: str
	pw: str

@app.post("/api/pre-register")
def PreRegisterHandler(json: pre_registerStruct, cookie: Union[str, None] = Cookie(default=None)):
	return pre_register.handler(json, cookie)

@app.post("/api/register")
def RegisterHandler(cookie: Union[str, None] = Cookie(default=None)):
	return {"a", "b"}

@app.post("/api")
def apiHandler(cookie: Union[str, None] = Cookie(default=None)):
	return {"a", "b"}





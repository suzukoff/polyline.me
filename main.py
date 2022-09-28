from typing import Union
from fastapi import *
from fastapi.responses import *
from pydantic import BaseModel
from enum import Enum

import app.index as index
import app.web as web
import app.profile as profile
import app.chat as chat
import app.conversation as conversation
import app.history as history

# 環境変数を共有
import app.global_var as g

# アプリケーションオブジェクトインスタンスの生成
app = FastAPI()


@app.get("/api/whoami")
def indexHandler():
	return {"a", "b"}





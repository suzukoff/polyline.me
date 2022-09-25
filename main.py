from typing import Union
from fastapi import FastAPI, Header, Response, status
from fastapi.responses import FileResponse
from pydantic import BaseModel
from enum import Enum

import app.index as index
import app.web as web

# 環境変数を共有
import app.global_var as g

# アプリケーションオブジェクトインスタンスの生成
app = FastAPI()


# インデックスページ
@app.get("/")
def indexHandler():
    return FileResponse(g.WWWROOT + "html/index/index.html")



# 静的ファイル
@app.get("/web/{webPath:path}")
def webHandler(webPath: str, response: Response):
    return web.handler(webPath, response)



# メンバー限定ページ
class memberOnly(str, Enum):
    profile = "profile",
    chat = "chat",
    conversation = "conversation"
    history = "history",


@app.get("/{directive}")
def hello_world(directive:memberOnly):
    if directive == memberOnly.profile:
        result = profile.handler()
    elif directive == memberOnly.chat:
        result = chat.handler()
    elif directive == memberOnly.conversation:
        result = conversation.handler()
    elif directive == memberOnly.history:
        result = history.handler()
    else:
        # 例外
    return result

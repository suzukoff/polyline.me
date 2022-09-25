from typing import Union
from fastapi import *
from fastapi.responses import *
from pydantic import BaseModel
from enum import Enum

import app.index as index
import app.web as web

# 環境変数を共有
import app.global_var as g

# アプリケーションオブジェクトインスタンスの生成
app = FastAPI()




# インデックスページ
@app.get("/index")
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
    return ""
    # if directive == memberOnly.profile:
    #     result = profile.handler()
    # elif directive == memberOnly.chat:
    #     result = chat.handler()
    # elif directive == memberOnly.conversation:
    #     result = conversation.handler()
    # elif directive == memberOnly.history:
    #     result = history.handler()
    # else:
    #     # 例外
    # return result



# バリデーションエラーハンドリング

from fastapi.exceptions import RequestValidationError

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_a, _b):
    return FileResponse(g.WWWROOT + "html/error/404.html")



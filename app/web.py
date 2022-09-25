import os
import re
from fastapi import FastAPI, Header, Response, status
from fastapi.responses import FileResponse

import app.global_var as g

def handler(webPath, response):


	# 【ディレクトリトラバーサル攻撃対策】-> ドット連続を禁止
	if re.match(r'\.{2,}', webPath):
		response.status_code = status.HTTP_404_NOT_FOUND
		return ""

	filepath = g.WWWROOT + webPath

	# 指定したファイルが存在しなければ、、、
	if not os.path.isfile(filepath):
		response.status_code = status.HTTP_404_NOT_FOUND
		return ""

	return FileResponse(filepath)




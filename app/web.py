from fastapi import FastAPI, Header, Response, status
import os

def handler(webPath, response):
	WWWROOT = os.environ.get("WWWROOT")

	extension = os.path.splitext(webPath)[1][1:]

	extDict = {
		"html": "text/html",
		"css": "text/css",
		"py": "text/py-script"
	}

	if (extension not in extDict):
		response.status_code = status.HTTP_404_NOT_FOUND
		return ""

	response.headers["Content-Type"] = ""

	return WWWROOT



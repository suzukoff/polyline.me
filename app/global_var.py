import os
from dotenv import load_dotenv


# 環境変数の読み込み
load_dotenv()
WWWROOT = os.environ.get("WWWROOT")
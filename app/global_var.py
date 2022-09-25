import os
from dotenv import load_dotenv


# 環境変数の読み込み
load_dotenv()
ROOT = os.environ.get("ROOT")
WWWROOT = ROOT + "web/"
DBROOT = ROOT + "db/"

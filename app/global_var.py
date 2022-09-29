import os
from dotenv import load_dotenv


# 環境変数の読み込み
load_dotenv()
ROOT = os.environ.get("ROOT")
WWWROOT = ROOT + "web/"
DBROOT = ROOT + "db/"

DOMAIN = os.environ.get("DOMAIN")

# SMTP関連
SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

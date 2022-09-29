import sqlite3
import app.global_var as g
import random, string
import re

# SMTP関連
import smtplib
from email.mime.text import MIMEText
 

def token_gen():
	randlst = [random.choice(string.ascii_letters + string.digits) for i in range(32)]
	return ''.join(randlst)

def handler(json, cookie):
	mail = json.mail
	pw = json.pw
	print(mail)

	# メールアドレスの文字数不正
	if not(10 <= len(mail) <= 100):
		return {
			"successed": False,
			"error": "メールアドレスは10文字以上100文字以内で入力してください。",
		}
	
	# メールアドレスの形式不正
	if not re.match(r'^[a-zA-Z0-9_.+-]+[a-zA-Z0-9_]@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$', mail):
		return {
			"successed": False,
			"error": "メールアドレスの形式が不正です。",
		}

	dbname = g.DBROOT + "polyline.db"
	connection = sqlite3.connect(dbname)
	cursor = connection.cursor()

	cursor.execute("SELECT mail FROM member WHERE mail = ?;", (mail, ))

	if cursor.fetchone() != None:
		# すでに登録されている場合
		connection.close()
		return {
			"successed": False,
			"error": "メールアドレスは既に登録されています。",
		}

	connection.close()

	# 仮登録処理へ
	# 1. トークンの生成
	# 2. トークンを含んだ仮会員登録メールの送信
	# 3. トークンをデータベースに登録

	# 1. トークンの生成
	token = token_gen()

	# 2. トークンを含んだ仮会員登録メールの送信
	try:
		mail_from = "register@" + g.DOMAIN
		
		# MIMETextを作成
		message = "以下のURLをクリックして会員登録を完了させてください。\n※ リンクの有効期限は1時間です。\n\n\n{}".format(token)
		msg = MIMEText(message, "text")
		msg["Subject"] = "【polyline】仮会員登録"
		msg["To"] = mail
		msg["From"] = mail_from
		
		server = smtplib.SMTP(g.SMTP_SERVER, g.SMTP_PORT)
		server.login(mail_from, g.SMTP_PASSWORD)
		server.send_message(msg)

		server.quit()

	except:
		# メールの送信に失敗しました。
		return {
			"successed": False,
			"error": "メールアドレスの送信に失敗しました。\nお手数をおかけしますが、時間をおいてお試しください。"
		}


	# 3. トークンをデータベースに登録

	# dbname = g.DBROOT + "polyline.db"
	# connection = sqlite3.connect(dbname)
	# cursor = connection.cursor()
	
	# cursor.execute("INSERT INTO pre_register;", (mail, ))

	# if cursor.fetchone() != None:
	# 	# すでに登録されている場合
	# 	connection.close()
	# 	return {
	# 		"successed": False,
	# 		"error": "メールアドレスは既に登録されています。",
	# 	}

	connection.close()



def handler():
	# メールアドレスの文字数不正
	if not(10 <= len(mail) <= 100):
		return {
			"successed": False,
			"error": "メールアドレスは10文字以上100文字以内で入力してください。",
		}

	# パスワードの文字数不正
	if not(8 <= len(pw) <= 32):
		return {
			"successed": False,
			"error": "パスワードは8文字以上32文字以内で入力してください。",
		}
	
	# メールアドレスの形式不正
	if not re.match(r'^[a-zA-Z0-9_.+-]+[a-zA-Z0-9_]@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$', mail):
		return {
			"successed": False,
			"error": "メールアドレスの形式が不正です。",
		}

	# パスワードの形式不正
	if not re.match(r'^[!-~]+$', pw):
		return {
			"successed": False,
			"error": "パスワードの形式が不正です。",
		}


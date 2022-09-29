"use strict";



(() => { // ログイン・登録フォームの操作
	const [loginTab, registerTab, loginForm, registerForm, login_mail, login_pw, register_mail, loginWarning, registerWarning, loginButton, registerButton] = getElm(["loginTab", "registerTab", "login_form", "register_form", "login_mail", "login_pw", "register_mail", "loginWarning", "registerWarning", "loginButton", "registerButton"])
	loginTab.addEventListener("click", function() {
		if (IsFb) return;
		loginForm.classList.add("selected");
		registerForm.classList.remove("selected");
		loginTab.classList.add("selected");
		registerTab.classList.remove("selected");
	});
	registerTab.addEventListener("click", function() {
		if (IsFb) return;
		loginForm.classList.remove("selected");
		registerForm.classList.add("selected");
		loginTab.classList.remove("selected");
		registerTab.classList.add("selected");
	});
	loginTab.click(); // 最初はログインフォームを表示した状態に

	function loginChecker() {
		if (!(login_mail_ok && login_pw_ok)) return;
		loginButton.classList.add("ok");
		loginWarning.textContent = "";
		loginWarning.classList.remove("warning");
	}

	// ログイン用メールアドレスチェック
	let login_mail_ok = false;
	login_mail.addEventListener("change", function() {
		loginButton.classList.remove("ok");
		login_mail_ok = false;
		if (this.value === "") {
			loginWarning.textContent = "";
			loginWarning.classList.remove("warning");
		}
		if (!mailCheck(this.value)) {
			loginWarning.textContent = "メールアドレスの形式が不正です。";
			loginWarning.classList.add("warning");
			return;
		}
		if (!between(10, 100)(this.value)) {
			loginWarning.textContent = "メールアドレスは10文字以上、100文字以内で入力してください。";
			loginWarning.classList.add("warning");
			return;
		}
		loginWarning.classList.remove("warning");
		loginWarning.textContent = "";
		login_mail_ok = true;
		loginChecker();
	});

	// ログイン用パスワードチェック
	let login_pw_ok = false;
	login_pw.addEventListener("change", function() {
		loginButton.classList.remove("ok");
		login_pw_ok = false;
		if (this.value === "") {
			loginWarning.textContent = "";
			loginWarning.classList.remove("warning");
		}
		if (!asciiCheck(this.value)) {
			loginWarning.textContent = "パスワードは半角英数字と記号のみで構成してください。";
			loginWarning.classList.add("warning");
			return;
		}
		if (!between(8, 32)(this.value)) {
			loginWarning.textContent = "パスワードは8文字以上、32文字以下で入力してください。";
			loginWarning.classList.add("warning");
			return;
		}
		loginWarning.classList.remove("warning");
		loginWarning.textContent = "";
		login_pw_ok = true;
		loginChecker();	
	});

	// 新規登録用メールアドレスチェック
	register_mail.addEventListener("change", function() {
		console.log(1);
		registerButton.classList.remove("ok");
		if (this.value === "") {
			registerWarning.textContent = "";
			registerWarning.classList.remove("warning");
		}
		if (!mailCheck(this.value)) {
			registerWarning.textContent = "メールアドレスの形式が不正です。";
			registerWarning.classList.add("warning");
			return;
		}
		if (!between(10, 100)(this.value)) {
			registerWarning.textContent = "メールアドレスは10文字以上、100文字以内で入力してください。";
			registerWarning.classList.add("warning");
			return;
		}
		registerButton.classList.add("ok");
		registerWarning.textContent = "";
		registerWarning.classList.remove("warning");
	});

	// ログイン処理
	loginButton.addEventListener("click", function() {
		if (!this.classList.contains("ok")) return;
		const data = {
			"mail": login_mail,
			"pw": login_pw,
		};
		HttpClient.Post("/api/login", data)
		.then(json => {

		})
		.catch(ex => {

		});
	});

	registerButton.addEventListener("click", function() {
		if (!this.classList.contains("ok")) return;
	});


})();




# talk-with

「Python」×「FastAPI」×「SQLite」で構成された超軽量なオープンソースのチャットアプリ。


# 環境情報

| 機能 | バージョン |
| ---- | ---- |
| Linux/Ubuntu | 22.04 |
| Python | 3.10.4 |
| SQLite | 3.37.2 |


# 環境構築手順


## 環境変数の登録

以下の環境変数を登録します。

```env
WWWROOT = "★talk-with/webディレクトリまでのパス(最後に「/」を付けて下さい。)★"
```

## Pythonパッケージのインストール

次に必要なPythonパッケージをインストールします。

```bash
pip install -r requirements.txt
```

## SQLiteのインストール

```bash
sudo apt install -y sqlite3
# インストールはすべてデフォルトで行います。
```

以下のコマンドで正しくインストールされていることを確認します。

```bash
sqlite3 --version
# -> 3.37.2
```

## Nginxのインストール

```bash
# Nginxのインストール
sudo apt install nginx

# Nginxの起動
sudo systemctl start nginx
```

「/etc/nginx/nginx.conf」ファイルのhttpディレクティブ内に以下の記載をします。

```nginx.conf
include </dev/nginx.confへのパス>;
```

```bash
# Nginxの再起動
sudo systemctl restart nginx
```

### Nginx動作までの設定

1. WWWROOTディレクティブまでの全てのディレクトリの実行権限を付与
2. 読み込み権限を対象ファイル全てに付与


## 証明書の発行

無料で使用できる「Let's Encrypt」を使用します。

```bash
sudo apt install certbot
 sudo certbot certonly --standalone -d polyline.me
```


# 実行方法

talk-withをカレントディレクトリとして状態で、以下のコマンドを実行します。

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

これで、サーバが起動します。


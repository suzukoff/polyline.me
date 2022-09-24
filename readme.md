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


# 実行方法

talk-withをカレントディレクトリとして状態で、以下のコマンドを実行します。

```bash
uvicorn main:app
```

これで、サーバが起動します。


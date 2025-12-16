flaskrの一つ上のディレクトリで仮想環境をオン
python3 -m venv venv
source venv/bin/activate
Flaskアプリケーションの場所を指定
次に、Flaskに対して、アプリケーションがどこにあるかを環境変数を使って教えます。

Linux や macOS の場合:
export FLASK_APP=flaskr

Windows (PowerShell) の場合:
$env:FLASK_APP = "flaskr"

Windows (コマンドプロンプト) の場合:
set FLASK_APP=flaskr

これは、「アプリケーションは flaskr という名前のパッケージの中にあるよ」と設定しています。

flask run

初期
flaskrの上の階層
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install Flask
python3 -c "from flaskr import db; db.create_todos_table()"
export FLASK_APP=flaskr
flask run

2回目以降
source venv/bin/activate
export FLASK_APP=flaskr
flask run
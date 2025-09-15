from flask import Flask
app = Flask(__name__)
# app.config['DEBUG'] = True  

import flaskr.main

# from flaskr import db
# # データベースのテーブルを作成する関数を呼び出す
# db.create_todos_table()
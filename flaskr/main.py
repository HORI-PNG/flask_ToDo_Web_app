from flask import render_template, request, redirect, url_for
import sqlite3
from flaskr import app  # __init__.pyで作成したappをインポート

DATABASE = 'database.db'

# '/' (ルートURL) にアクセスされたら、ToDoリストを表示する
@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # カラム名でデータを取り出せるようにする
    todos = conn.execute("SELECT * FROM todos ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

# タスクを追加する (index.htmlの追加フォームから呼ばれる)
@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form['task'] # フォームからタスク内容を取得
    conn = sqlite3.connect(DATABASE)
    conn.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    return redirect(url_for('index')) # トップページにリダイレクト

# タスクの状態を更新する (完了/未完了ボタンから呼ばれる)
@app.route('/update/<int:id>', methods=['POST'])
def update_todo(id):
    conn = sqlite3.connect(DATABASE)
    # 現在の状態を取得
    cur = conn.cursor()
    status = cur.execute("SELECT status FROM todos WHERE id = ?", (id,)).fetchone()[0]
    
    # 状態を反転させる
    new_status = '完了' if status == '未完了' else '未完了'
    
    conn.execute("UPDATE todos SET status = ? WHERE id = ?", (new_status, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# タスクを削除する (削除ボタンから呼ばれる)
@app.route('/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    conn = sqlite3.connect(DATABASE)
    conn.execute("DELETE FROM todos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
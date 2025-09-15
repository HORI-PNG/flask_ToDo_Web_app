import sqlite3

DATABASE = 'database.db'

def create_todos_table():
    conn = sqlite3.connect(DATABASE)
    # ToDoを管理するテーブルを作成
    # ID(主キー、自動増分)、task(タスク内容)、status(状態、デフォルトは'未完了')
    conn.execute(
        "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL, status TEXT NOT NULL DEFAULT '未完了')"
    )
    conn.close()
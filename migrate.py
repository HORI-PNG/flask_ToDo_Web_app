# 何か追加したいものがあればここに記述
import sqlite3

DATABASE = 'database.db'

def migrate():
    conn = sqlite3.connect(DATABASE)
    # todosテーブルに priority カラム（文字列型、デフォルト値 '中'）を追加
    try:
        conn.execute("ALTER TABLE todos ADD COLUMN priority TEXT DEFAULT '中'")
        conn.commit()
        print("Successfully added priority column.")
    except sqlite3.OperationalError:
        print("Column might already exist.")
    finally:
        conn.close()

if __name__ == '__main__':
    migrate()
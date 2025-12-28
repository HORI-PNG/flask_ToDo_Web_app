1. SQLiteの仕組み
・「SQLite」は、一般的なデータベース（PostgreSQLやMySQLなど）とは異なり、「サーバー」を必要としないファイルベースのデータベースである。
　→ 1ファイル＝1データベース：プロジェクト内にある「database.db」という1つのファイルの中に、すべてのデータとテーブル構造が保存されている
　→ 管理が容易：サーバーの設定が不要で、ファイルをコピーするだけでバックアップや移行が完了する
　→ Python標準ライブラリ:
Pythonに標準で組み込まれている「sqlite3」モジュールを使用して操作するため、追加のインストールなしで使える

2. SQL文法の解説
コード内で使われている主要な4つの操作（CRUD）について

% テーブルの作成（Create）%
flaskr/db.py

CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    task TEXT NOT NULL, 
    status TEXT NOT NULL DEFAULT '未完了'
)

・IF NOT EXISTS：テーブルが既に存在する場合は何もしないという
・id INTEGER PRIMARY KEY AUTOINCREMENT：各タスクを識別する一意の番号。新しいデータが入るたびに自動で 1, 2, 3...と増える
・TEXT NOT NULL：文字列型のデータで、空（NULL）であってはいけないという制約
・DEFAULT '未完了'：データ追加時に状態が指定されない場合、自動的に「未完了」になる

% データの取得（Read） %
flaskr/main.pyのindex()

def index():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # カラム名でデータを取り出せるようにする
    todos = conn.execute("SELECT * FROM todos ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

・SELECT * FROM todos ORDER BY id DESC：todosテーブルからすべてのカラム（*）を取得し、IDの大きい順（新しい順）に並べ替える

% データの追加（Insert） %
flaskr/main.pyのadd_todo()

def add_todo():
    task = request.form['task'] # フォームからタスク内容を取得
    conn = sqlite3.connect(DATABASE)
    conn.execute("INSERT INTO todos (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    return redirect(url_for('index')) # トップページにリダイレクト

・INSERT INTO todos (task) VALUES (?)：taskカラムに値を入れます。? はプレースホルダと呼ばれ、後からPythonの変数（タスク内容）を安全に流し込むための仕組みです。

% データの更新・削除（Update / Delete） %
update_todoやdelete_todo()

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

def delete_todo(id):
    conn = sqlite3.connect(DATABASE)
    conn.execute("DELETE FROM todos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

・UPDATE todos SET status = ? WHERE id = ?：指定した id のデータの status を書き換える
・DELETE FROM todos WHERE id = ?：指定した id の行を完全に削除する


% 作成の注意点 %
SQLiteでは、プログラムを書き換えただけでは既存のdatabase.dbファイルの中身は変わらない
→ 一度database.dbファイルを削除して再度アプリを実行する or memo.mdにある初期化コマンドを実行してテーブルを作り直す
→ SQLの「ALTER TABLE」文を使って、既存のテーブルにカラムを追加する
# バックエンド：
* ・Flask（Pythonのフレームワーク）
* ・dbの操作やページ生成
# フロントエンド：
* ・HTML5, CSS3, jinja2（Flask標準テンプレートエンジン）
* ・{% for ... %}や{{...}}のように記述することで、バックエンドから渡されたデータを動的に表示している

# ライブラリ：
* ・Flask：Webアプリケーション本体を構築するためのフレームワーク
* ・sqlite3：Python標準ライブラリ。SQLiteを操作するため
* ・Jinja2：Flask標準テンプレートエンジン。HTMLファイルを動的に生成
* ・Werkzeug / ItsDangerous / Click / MarkupSafe / Blinker：Flaskが内部で依存している標準的なライブラリ群

## コード説明：
* ・__init__.py：アプリケーションの初期化。Flask(__name__)でアプリ本体(app)を生成
* ・main.py：
アプリの心臓部。ルート（URL）にアクセスが来た時の処理
* 　→ @app.route('/')：ToDo一覧を表示。dbから全データを取得してindex.htmlに渡す
* 　→ @app.route('/add', methods=['POST'])：新しいタスクをdbに挿入
* 　→ @app.route('/update/<int:id>', methods=['POST'])：指定されたIDのタスクのstatusを反転
* 　→ @app.route('/delete/<int:id>', methods=['POST'])：タスクを削除
* ・templates/index.html：
* 　→ {% for todo in todos %}：dbから取得したデータの数だけループして、ToDoリストの項目を表示
* 　→ {% if todo.status == '完了' %}completed{% endif %}：完了状態であればCSSクラスcompletedを付与し、打ち消し線を引くなどの装飾を行う
* ・static/style.css：
* 　→ flexbox を多用して、中央揃えのモダンなカードデザインを実現
* 　→ .todo-item.completed .task-text で、完了したタスクの装飾
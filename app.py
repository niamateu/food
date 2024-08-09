from flask import Flask,render_template,request
import random

# アプリのインスタンス作成
app = Flask(__name__)

# メニューリスト
menu = ["海鮮丼","生姜焼き","牛丼","ハンバーグ","パスタ","カレー","ラーメン","コンビニ弁当"]

# リストからランダムに1つメニューを選びselect_menu変数に代入
@app.route('/', methods=['GET','POST'])
def index():
        select_menu = None
        if request.method == 'POST':
                select_menu = random.choice(menu)
        return render_template('index.html',select_menu=select_menu)

# アプリをデバックモードで起動
if __name__=='__main__':
        app.run(debug=True)
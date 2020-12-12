# ライブラリのinport json リンク読み込み randam 軽量フレームワーク bs4
import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template 
from bs4 import BeautifulSoup


# flaskのフレームワーク
app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")



@app.route("/api/recommend_article")
def api_recommend_article():
        # 1. はてブのホットエントリーページのHTMLを取得する
    with urlopen("http://feeds.feedburner.com/hatena/b/hotentry") as res:
        html = res.read().decode('utf-8')
        # 2. BeautifulSoupでHTMLを読み込む
        soup = BeautifulSoup(html, "html.parser")
        # 3. 記事一覧を取得する
        items = soup.select('item')
        # 4. ランダムに1件取得する
        shuffle(items)
        item = items[0]
        print(item)

        # 5. 以下の形式で返却する.
        return json.dumps({
            "content" : item.find("title").string,
            # "link" : item.find("link").string
            "link": item.get('rdf:about')
    })



@app.route("/api/xxxx")
def api_xxxx():
    """
        **** ここを実装します（発展課題） ****
    """
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5004)

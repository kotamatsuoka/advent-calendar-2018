import json
import requests
import jwt
from flask import Flask, request
from flask import render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "sample1216"

LINE_CHANNEL_ID = "自身のチャネルID"
LINE_CHANNEL_SECRET = "自身のチャネルシークレット"
REDIRECT_URL = "設定したリダイレクト先のURL"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html",
                           random_state="line1216",
                           channel_id=LINE_CHANNEL_ID,
                           redirect_url=REDIRECT_URL)


@app.route("/line/login", methods=["GET"])
def line_login():
    # 認可コードを取得する
    request_code = request.args["code"]
    uri_access_token = "https://api.line.me/oauth2/v2.1/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data_params = {
        "grant_type": "authorization_code",
        "code": request_code,
        "redirect_uri": REDIRECT_URL,
        "client_id": LINE_CHANNEL_ID,
        "client_secret": LINE_CHANNEL_SECRET
    }

    # トークンを取得するためにリクエストを送る
    response_post = requests.post(uri_access_token, headers=headers, data=data_params)
    # 今回は"id_token"のみを使用する
    line_id_token = json.loads(response_post.text)["id_token"]

    # ペイロード部分をデコードすることで、ユーザ情報を取得する
    decoded_id_token = jwt.decode(line_id_token,
                                  LINE_CHANNEL_SECRET,
                                  audience=LINE_CHANNEL_ID,
                                  issuer='https://access.line.me',
                                  algorithms=['HS256'])

    return render_template("line_success.html", user_profile=decoded_id_token)


if __name__ == '__main__':
    app.run(debug=True)

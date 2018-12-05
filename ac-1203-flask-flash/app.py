from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "sample1203"


@app.route("/", methods=["GET", "POST"])
def index():
    username = ""
    text = ""
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        if request.form["username"] and request.form["text"]:
            username = request.form["username"]
            text = request.form["text"]
            flash("投稿を成功しました＼(^o^)／", "success")
        if request.form["username"] == "":
            flash("ユーザー名を入力してください。", "failed")
        if request.form["text"] == "":
            flash("テキストを入力してください。", "failed")

        return render_template("index.html", username=username, text=text)


if __name__ == "__main__":
    app.run()

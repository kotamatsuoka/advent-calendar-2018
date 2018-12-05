# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from flask import Flask, request
from flask import render_template

from blog_form import BlogForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "sample1201"

@app.route("/", methods=["GET", "POST"])
def index():
    form = BlogForm()
    if request.method == "GET":
        message = "フォームを送ってみよう！！"
        return render_template("index.html", form=form, message=message)

    if request.method == "POST":
        if form.validate_on_submit():
            message = "バリデーションを通ったよ＼(^o^)／"
            return render_template("index.html", form=form, message=message)

        message = "バリデーションに失敗したよ(T_T)"
        return render_template("index.html", form=form, message=message)

if __name__ == '__main__':
    app.run(debug=True)

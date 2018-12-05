from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "sample1204"


@app.route("/", methods=["GET"])
def index():
    username = "Kota"
    birth_day = {"year": 2000, "month": 11, "day": 25}
    actresses = ["有村架純", "中条あやみ", "石原さとみ"]
    comedians = ["和牛", "ジャルジャル", "霜降り明星"]

    return render_template("index.html",
                           username=username, birth_day=birth_day,
                           actresses=actresses, comedians=comedians)


if __name__ == "__main__":
    app.run()

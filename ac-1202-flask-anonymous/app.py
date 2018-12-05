from flask import Flask, render_template
from flask_login import LoginManager, current_user

from custom_anonymous_user import CustomAnonymousUser

app = Flask(__name__)
app.config["SECRET_KEY"] = "sample1202"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.anonymous_user = CustomAnonymousUser

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

import os
import sys

from ac_1215_DDD_application_service.user_application_service import UserApplicationService
from ac_1215_DDD_application_service.user_repository import InMemoryUserRepository

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "sample1215"


@app.route("/", methods=["GET"])
def index():
    in_memory_user_repository = InMemoryUserRepository()
    user_application_service = UserApplicationService(in_memory_user_repository)
    user_list = user_application_service.find_all()

    return render_template("index.html", user_list=user_list)


if __name__ == '__main__':
    app.run(debug=True)

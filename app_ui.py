from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from app_lookup import custom_lookup

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", debug=True)

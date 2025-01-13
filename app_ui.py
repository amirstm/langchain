from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from app_lookup import custom_lookup

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = custom_lookup(name=name)
    return jsonify(
        {"summary_and_facts": summary.to_dict(), "picture_url": profile_pic_url}
    )


### TRACE ACTIVATED ###
if __name__ == "__main__":
    app.run(host="localhost", debug=True)

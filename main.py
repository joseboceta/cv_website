import os
from flask import (Flask, render_template, send_from_directory, url_for)

app = Flask(__name__)
app.debug = False
app.secret_key = os.urandom(12)

# ENDPOINTS
@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/download/cv', methods=["GET"])
def download_cv():
    return send_from_directory(directory="static/downloads", filename="cv.pdf")

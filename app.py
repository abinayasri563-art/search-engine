import math
import os
import shutil
from collections import defaultdict, Counter
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    return "You searched for: " + str(query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

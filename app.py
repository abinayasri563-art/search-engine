import math
import os
import shutil
from collections import defaultdict, Counter
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("query")
    return f"You searched for: {query}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

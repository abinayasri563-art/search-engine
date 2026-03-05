import math
import os
import shutil
from collections import defaultdict, Counter
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("query", "")
        return render_template(
            "index.html",
            doc_count=0,
            vocab_size=0,
            results={
                "ranked": [("sample_doc.txt", 0.95, "default")],
                "best_score": 0.95,
                "result_msg": f"Results for '{query}'"
            },
            query_input=query,
            query_terms=query.split(),
            tables=None
        )

    return render_template(
        "index.html",
        doc_count=0,
        vocab_size=0,
        results=None,
        query_input="",
        query_terms=[],
        tables=None
    )

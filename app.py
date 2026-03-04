import math
import os
import shutil
from collections import defaultdict, Counter
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your-secret-key"  # required if using flash()

# Example route
@app.route("/")
def home():
    return "Search Engine v2 is running!"

# Add other routes here, e.g., for uploading documents, searching, etc.

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway dynamic port
    app.run(host="0.0.0.0", port=port, debug=True)
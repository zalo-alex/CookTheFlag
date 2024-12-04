from flask import Flask, render_template
from src.module_manage import ModuleManage

import base64
import re

app = Flask(__name__)
manager = ModuleManage()

@app.route("/")
def index():
    return render_template("index.html", modules=manager.modules, categories=manager.categories)

@app.route("/regex/<b64_query>")
def regex(b64_query):
    query = base64.b64decode(b64_query.encode()).decode()
    matches = []

    for r in manager.regexs:
        if not r:
            continue

        if r.match(query):
            matches.append({
                "url": manager.regexs[r].url,
                "name": manager.regexs[r].name
            })
        
    return {
        "matches": matches
    }

if __name__ == "__main__":
    manager.import_all(app)
    app.run(host="0.0.0.0", port=8080, debug=True)

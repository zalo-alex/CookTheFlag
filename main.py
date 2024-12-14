from flask import Flask, render_template
from src.module_manage import ModuleManage

import base64

app = Flask(__name__)
manager = ModuleManage()

@app.errorhandler(404) 
def not_found(e): 
    return render_template("404.html", modules=manager.modules, categories=manager.categories) 

@app.route("/")
def index():
    return render_template("index.html", modules=manager.modules, categories=manager.categories)

@app.route("/regex/<b64_query>")
def regex(b64_query):
    query = base64.b64decode(b64_query.encode()).decode()
    matches = []

    for r in manager.regexs:
        regex = r["regex"]

        if regex.match(query):
            module = r["module"]
            matches.append({
                "url": module.url,
                "name": module.name,
                "id": r.get("id"),
                "element_name": r.get("element_name")
            })
        
    return {
        "matches": matches
    }

if __name__ == "__main__":
    manager.import_all(app)
    app.run(host="0.0.0.0", port=8080, debug=True)

from flask import Flask, render_template
from src.module_manage import ModuleManage

app = Flask(__name__)
manager = ModuleManage()

@app.route("/")
def index():
    return render_template("index.html", modules=manager.modules, categories=manager.categories)

if __name__ == "__main__":
    manager.import_all(app)
    app.run(host="0.0.0.0", port=80, debug=True)
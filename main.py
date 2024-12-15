import traceback
from flask import Flask, render_template
from flask_sock import Sock
from types import GeneratorType

from src.module_manage import ModuleManage

import base64
import json

app = Flask(__name__)
sock = Sock(app)

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

@sock.route('/ws')
def ws(sock):
    while True:
        payload = json.loads(sock.receive())
        print(payload)
        type = payload.get("type")
        payload = payload.get("payload")
        
        if not type or not payload:
            continue
        
        if type == "submit":
            module = payload.get("module")
            if not module or module not in manager.modules:
                continue
            
            module = manager.modules[module]            
            type = payload.get("type")
            data = payload.get("data")
            
            for element in module.layout:
                if element.parser:
                    data[element.id] = element.parser.parse(data[element.id])
            
            try:
                res = module.submit(type, data)
                
                if isinstance(res, GeneratorType):
                    for r in res:
                        sock.send(json.dumps({
                            "type": "response", "data": r
                        }))
                    sock.send(json.dumps({"type": "done"}))
                else:
                    sock.send(json.dumps({
                        "type": "response", "data": res
                    }))
                    sock.send(json.dumps({"type": "done"}))
            except Exception as e:
                traceback.print_exc()
                return {"__error": str(e)}

if __name__ == "__main__":
    manager.import_all(app)
    app.run(host="0.0.0.0", port=8080, debug=True)

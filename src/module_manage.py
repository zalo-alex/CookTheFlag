import re
from flask import render_template, request

from copy import deepcopy

import glob
import os
import importlib

class ModuleManage:
    
    def __init__(self):
        self.modules_folder = "modules"
        self.modules = {}
        self.categories = {}
        self.regexs = {}
    
    def add_to_category(self, category, module):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(module)
    
    def route(self, module):
        
        def route():
            if request.method == "GET":
                return render_template("module.html", module=module, modules=self.modules, categories=self.categories)
            elif request.method == "POST":
                type = request.json.get("type")                
                return module.submit(type, request.json)
        
        return route
    
    def import_all(self, app):
        for module_file in glob.glob(f"{self.modules_folder}/*.py"):

            module_name = os.path.basename(module_file)[:-3]
            custom_module = importlib.import_module(f"{self.modules_folder}.{module_name}").CustomModule
            custom_module.url = module_name

            print(f" + Imported: {custom_module.name} (/module/{module_name})")

            self.modules[module_name] = custom_module
            if custom_module.regex:
                self.regexs[re.compile(custom_module.regex)] = custom_module
            self.add_to_category(custom_module.category, module_name)

            app.add_url_rule(f"/module/{module_name}", view_func=self.route(custom_module), methods=["GET", "POST"], endpoint=f"module_{module_name}")
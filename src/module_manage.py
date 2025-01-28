import base64
import re
from flask import render_template, request, flash, redirect

from src.auth import is_logged

import glob
import os
import importlib
import traceback

class ModuleManage:
    
    def __init__(self):
        self.modules_folder = "modules"
        self.modules = {}
        self.categories = {}
        self.regexs = []
    
    def add_to_category(self, category, module):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(module)
    
    def route(self, module):
        
        def get():
            decoded_args = {}
            for key, value in request.args.items():
                decoded_args[key] = base64.b64decode(value).decode('latin-1')
            
            if not module.script and not is_logged():
                flash("You need to be logged-in to use Server side modules", "info")
                return redirect("/login")

            return render_template("module.html", module=module, modules=self.modules, categories=self.categories, args=decoded_args)
        
        return get

    def find_regexs(self, module):
        for element in module.layout:
            if element.regex:
                self.regexs.append({
                    "regex": element.regex,
                    "module": module,
                    "id": element.id,
                    "element_name": element.name
                })
        if module.regex:
            self.regexs.append({
                "regex": module.regex,
                "module": module,
                "id": None,
            })
    
    def compile_parsers(self, module):
        for element in module.layout:
            if element.parser:
                element.parser._compile()
    
    def import_all(self, app):
        for module_file in glob.glob(f"{self.modules_folder}/*.py"):

            module_name = os.path.basename(module_file)[:-3]
            custom_module = importlib.import_module(f"{self.modules_folder}.{module_name}").CustomModule
            custom_module.url = module_name

            print(f" + Imported: {custom_module.name} (/module/{module_name})")

            self.modules[module_name] = custom_module
            self.find_regexs(custom_module)
            self.compile_parsers(custom_module)
            self.add_to_category(custom_module.category, module_name)

            app.add_url_rule(f"/module/{module_name}", view_func=self.route(custom_module), endpoint=f"module_{module_name}")
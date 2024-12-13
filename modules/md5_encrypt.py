from src.module import Module
from src.layout import *
from src.regexs import Regexs

import hashlib

class CustomModule(Module):
    name = "MD5 Encrypt"
    category = "Hashing"
    regex = Regexs.MD5
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("MD5 Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": hashlib.md5(data["input"].encode("latin1")).hexdigest()
        }
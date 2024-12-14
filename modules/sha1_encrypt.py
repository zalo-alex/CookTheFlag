from src.module import Module
from src.layout import *
from src.regexs import Regexs

import hashlib

class CustomModule(Module):
    name = "SHA-1 Encrypt"
    category = "hashing"
    regex = Regexs.SHA1
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("SHA-1 Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": hashlib.sha1(data["input"].encode("latin1")).hexdigest()
        }
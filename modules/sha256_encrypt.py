from src.module import Module
from src.layout import *
from src.regexs import Regexs

import hashlib

class CustomModule(Module):
    name = "SHA-256 Encrypt"
    category = "Hashing"
    regex = Regexs.SHA256
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("SHA-256 Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": hashlib.sha256(data["input"].encode("latin1")).hexdigest()
        }
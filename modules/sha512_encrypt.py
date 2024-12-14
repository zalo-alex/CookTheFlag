from src.module import Module
from src.layout import *
from src.regexs import Regexs

import hashlib

class CustomModule(Module):
    name = "SHA-512 Encrypt"
    category = "hashing"
    regex = Regexs.SHA512
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("SHA-512 Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": hashlib.sha512(data["input"].encode("latin1")).hexdigest()
        }
from src.module import Module
from src.layout import *
from src.regexs import Regexs

import hashlib

class CustomModule(Module):
    name = "Blake2b Encrypt"
    category = "Hashing"
    regex = Regexs.BLAKE2B
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("Blake2b Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": hashlib.blake2b(data["input"].encode("latin1")).hexdigest()
        }
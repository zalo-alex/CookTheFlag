from src.module import Module
from src.layout import *
from src.regexs import Regexs

import hashlib

class CustomModule(Module):
    name = "Blake2s Encrypt"
    category = "Hashing"
    regex = Regexs.BLAKE2S
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("Blake2s Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": hashlib.blake2s(data["input"].encode("latin1")).hexdigest()
        }
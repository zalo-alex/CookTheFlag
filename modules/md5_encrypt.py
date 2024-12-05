from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

import hashlib

class CustomModule(Module):
    name = "MD5 Encrypt"
    category = "Hashing"
    regex = r"^[a-fA-F0-9]{32}$"
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("MD5 Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": hashlib.md5(data["input"].encode("latin1")).hexdigest()
        }
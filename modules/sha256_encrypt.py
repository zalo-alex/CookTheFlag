from src.module import Module
from src.layout import *

import hashlib

class CustomModule(Module):
    name = "SHA-256 Encrypt"
    category = "Hashing"
    regex = r"^[a-fA-F0-9]{64}$"
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("SHA-256 Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": hashlib.sha256(data["input"].encode("latin1")).hexdigest()
        }
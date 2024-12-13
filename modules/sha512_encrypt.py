from src.module import Module
from src.layout import *

import hashlib

class CustomModule(Module):
    name = "SHA-512 Encrypt"
    category = "Hashing"
    regex = r"^[a-fA-F0-9]{128}$"
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("SHA-512 Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": hashlib.sha512(data["input"].encode("latin1")).hexdigest()
        }
from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

import hashlib

class CustomModule(Module):
    name = "Blake2s Encrypt"
    category = "Hashing"
    regex = r"^[a-fA-F0-9]{64}$"
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("Blake2s Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": hashlib.blake2s(data["input"].encode("latin1")).hexdigest()
        }
from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "ASCII to Hex"
    category = "encoding"
    layout = [
        Input("ASCII Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("Hex Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": data["input"].encode("latin-1").hex()
        }
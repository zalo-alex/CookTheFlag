from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "Hex to Number"
    category = "encoding"
    layout = [
        Input("Hex Input", "input", textarea=True, regex=r"[0-9a-fA-F]+"),
        Submit("Submit", "encode"),
        Input("Number Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": str(int(data["input"], 16))
        }
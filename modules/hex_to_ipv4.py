from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "Hex to IPv4"
    category = "encoding"
    layout = [
        Input("Hex Input", "input"),
        Submit("Submit", "encode"),
        Input("IPv4 Output", "output")
    ]
    
    def submit(type, data):
        parts = data["input"].split(".")
        return {
            "output": ".".join([ str(int(p, 16)) for p in parts ])
        }
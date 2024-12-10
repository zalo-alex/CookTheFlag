from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "Binary to IPv4"
    category = "encoding"
    layout = [
        Input("Binary Input", "input"),
        Submit("Submit", "encode"),
        Input("IPv4 Output", "output")
    ]
    
    def submit(type, data):
        parts = data["input"].split(".")
        print(parts)
        return {
            "output": ".".join([ str(int(p, 2)) for p in parts ])
        } 
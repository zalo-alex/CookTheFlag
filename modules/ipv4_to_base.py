from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "IPv4 to Base"
    category = "encoding"
    layout = [
        Input("IPv4 Input", "input"),
        Submit("Submit", "encode"),
        Input("Binary Output", "bin-output"),
        Input("Hex Output", "hex-output"),
    ]
    
    def submit(type, data):
        parts = data["input"].split(".")
        return {
            "bin-output": ".".join([ bin(int(p))[2:] for p in parts ]),
            "hex-output": ".".join([ hex(int(p))[2:] for p in parts ])
        }
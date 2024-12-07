from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "Number to Binary"
    category = "encoding"
    layout = [
        Input("Number Input", "input", textarea=True, regex=r"[0-9]+"),
        Submit("Submit", "encode"),
        Input("Binary Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": bin(int(data["input"]))[2:]
        }
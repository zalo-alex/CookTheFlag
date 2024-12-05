from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

import base64

class CustomModule(Module):
    name = "Base64 Encode"
    category = "encoding"
    regex=r"^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{4}|[A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{2}={2})$"
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("Base64 Output", "output", textarea=True),
    ]
    
    def submit(type, data):
        return {
            "output": base64.b64encode(data["input"].encode("latin-1")).decode("latin-1")
        }
from src.module import Module
from src.layout import *

class CustomModule(Module):
    name = "URL Decode"
    category = "encoding"
    layout = [
        Input("URL Encoded Input", "input", textarea=True),
        Submit("Submit", "encode", auto=True),
        Input("ASCII Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": decodeURI(data["input"])
        }
    """
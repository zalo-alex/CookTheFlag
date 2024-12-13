from src.module import Module
from src.layout import *

class CustomModule(Module):
    name = "Hex to Number"
    category = "encoding"
    layout = [
        Input("Hex Input", "input", textarea=True, regex=r"^[0-9a-fA-F]+$"),
        Submit("Submit", "encode"),
        Input("Number Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": parseInt(data["input"], 16)
        }
    """
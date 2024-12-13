from src.module import Module
from src.layout import *
from src.regexs import Regexs

class CustomModule(Module):
    name = "Binary to Decimal"
    category = "encoding"
    layout = [
        Input("Binary Input", "input", textarea=True, regex=Regexs.BIN),
        Submit("Submit", "encode"),
        Input("Decimal Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": parseInt(data["input"], 2)
        }
    """
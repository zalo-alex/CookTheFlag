from src.module import Module
from src.layout import *
from src.regexs import Regexs

class CustomModule(Module):
    name = "Hex to Decimal"
    category = "encoding"
    layout = [
        Input("Hex Input", "input", textarea=True, regex=Regexs.HEX),
        Submit("Submit", "encode"),
        Input("Decimal Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": parseInt(data["input"], 16)
        }
    """
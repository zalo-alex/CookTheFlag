from src.module import Module
from src.layout import *
from src.regexs import Regexs
from src.parsers import HexParser

class CustomModule(Module):
    name = "Hex to Decimal"
    category = "encoding"
    layout = [
        Input("Hex Input", "input", textarea=True, regex=Regexs.HEX, parser=HexParser()),
        Submit("Submit", "encode", auto=True),
        Input("Decimal Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": parseInt(data["input"], 16)
        }
    """
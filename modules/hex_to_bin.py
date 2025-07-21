from src.module import Module
from src.layout import *
from src.regexs import RegExs
from src.parsers import HexParser

class CustomModule(Module):
    name = "Hex to Binary"
    category = "encoding"
    layout = [
        Input("Hex Input", "input", textarea=True, regex=RegExs.HEX, parser=HexParser()),
        Submit("Submit", "encode", auto=True),
        Input("Binary Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": parseInt(data["input"], 16).toString(2)
        }
    """
from src.parsers import BinaryParser
from src.module import Module
from src.layout import *
from src.regexs import RegExs

class CustomModule(Module):
    name = "Binary to Decimal"
    category = "encoding"
    layout = [
        Input("Binary Input", "input", textarea=True, regex=RegExs.BIN, parser=BinaryParser()),
        Submit("Submit", "encode", auto=True),
        Input("Decimal Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": parseInt(data["input"], 2)
        }
    """
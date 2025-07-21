from src.module import Module
from src.layout import *
from src.regexs import RegExs
from src.parsers import BinaryParser

class CustomModule(Module):
    name = "Binary to Hex"
    category = "encoding"
    layout = [
        Input("Bin Input", "input", textarea=True, regex=RegExs.BIN, parser=BinaryParser()),
        Submit("Submit", "encode", auto=True),
        Input("Hex Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": parseInt(data["input"], 2).toString(16)
        }
    """
from src.module import Module
from src.layout import *
from src.regexs import RegExs
from src.parsers import BinaryParser

class CustomModule(Module):
    name = "Binary to ASCII"
    category = "encoding"
    layout = [
        Input("Bin Input", "input", textarea=True, regex=RegExs.BIN, parser=BinaryParser()),
        Submit("Submit", "encode", auto=True),
        Input("ASCII Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": data["input"].match(/.{8}/g).map((v) => String.fromCharCode(parseInt(v, 2))).join('')
        }
    """
from src.module import Module
from src.layout import *
from src.regexs import RegExs
from src.parsers import HexParser

class CustomModule(Module):
    name = "Hex to ASCII"
    category = "encoding"
    layout = [
        Input("Hex Input", "input", textarea=True, regex=RegExs.HEX, parser=HexParser()),
        Submit("Submit", "encode", auto=True),
        Input("ASCII Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": data["input"].match(/.{1,2}/g).map((v) => String.fromCharCode(parseInt(v, 16))).join('')
        }
    """
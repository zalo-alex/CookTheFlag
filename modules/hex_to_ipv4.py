from src.module import Module
from src.layout import *
from src.regexs import Regexs

class CustomModule(Module):
    name = "Hex to IPv4"
    category = "encoding"
    layout = [
        Input("IPv4 Hex Input", "input", regex=Regexs.IPV4_HEX),
        Submit("Submit", "encode"),
        Input("IPv4 Decimal Output", "output")
    ]
    script = """
        const parts = data["input"].split(".")
        const res = parts.map((p) => parseInt(p, 16))
        return {
            "output": res.join(".")
        }
    """
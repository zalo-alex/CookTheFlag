from src.module import Module
from src.layout import *

class CustomModule(Module):
    name = "Binary to IPv4"
    category = "encoding"
    layout = [
        Input("IPv4 Binary Input", "input"),
        Submit("Submit", "encode", auto=True),
        Input("IPv4 Decimal Output", "output")
    ]
    script = """
        const parts = data["input"].split(".")
        const res = parts.map((p) => parseInt(p, 2))
        return {
            "output": res.join(".")
        }
    """
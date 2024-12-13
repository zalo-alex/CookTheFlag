from src.module import Module
from src.layout import *

class CustomModule(Module):
    name = "Hex to IPv4"
    category = "encoding"
    layout = [
        Input("Hex Input", "input"),
        Submit("Submit", "encode"),
        Input("IPv4 Output", "output")
    ]
    script = """
        const parts = data["input"].split(".")
        const res = parts.map((p) => parseInt(p, 16))
        return {
            "output": res.join(".")
        }
    """
from src.module import Module
from src.layout import *

class CustomModule(Module):
    name = "ASCII to Hex"
    category = "encoding"
    layout = [
        Input("ASCII Input", "input", textarea=True),
        Submit("Submit", "encode", auto=True),
        Input("Hex Output", "output", textarea=True),
    ]
    script = """
        var input = data["input"]
        var res = input.split("").map((c) => c.charCodeAt(0).toString(16)).join("")
        return {
            "output": res
        }
    """
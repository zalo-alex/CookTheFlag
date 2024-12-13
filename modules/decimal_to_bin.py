from src.module import Module
from src.layout import *
from src.regexs import Regexs

class CustomModule(Module):
    name = "Decimal to Binary"
    category = "encoding"
    layout = [
        Input("Decimal Input", "input", textarea=True, regex=Regexs.DEC),
        Submit("Submit", "encode"),
        Input("Binary Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": parseInt(data["input"]).toString(2)
        }
    """
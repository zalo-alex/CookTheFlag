from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "Binary to Hex"
    category = "encoding"
    layout = [
        Input("Bin Input", "input", textarea=True, regex=r"[0-1]+"),
        Submit("Submit", "encode"),
        Input("Hex Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": parseInt(data["input"], 2).toString(16)
        }
    """
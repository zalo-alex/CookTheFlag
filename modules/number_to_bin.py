from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "Number to Binary"
    category = "encoding"
    layout = [
        Input("Number Input", "input", textarea=True, regex=r"[0-9]+"),
        Submit("Submit", "encode"),
        Input("Binary Output", "output", textarea=True),
    ]
    script = """
        return {
            "output": parseInt(data["input"]).toString(2)
        }
    """
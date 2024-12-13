from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "ASCII to Binary"
    category = "encoding"
    layout = [
        Input("ASCII Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("Binary Output", "output", textarea=True),
    ]
    script = """
        var input = data["input"]
        var res = input.split("").map((c) => c.charCodeAt(0).toString(2).padStart(8, '0')).join("")
        return {
            "output": res
        }
    """
from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "ASCII to Hex"
    category = "encoding"
    layout = [
        Input("ASCII Input", "input", textarea=True),
        Submit("Submit", "encode"),
        Input("Hex Output", "output", textarea=True),
    ]
    script = """
        var input = data["input"]
        var res = ""
        for (let i = 0; i < input.length; i++) {
            res += input[i].charCodeAt(0).toString(16)
        }
        return {
            "output": res
        }
    """
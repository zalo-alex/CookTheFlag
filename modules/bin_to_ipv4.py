from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit

class CustomModule(Module):
    name = "Binary to IPv4"
    category = "encoding"
    layout = [
        Input("Binary Input", "input"),
        Submit("Submit", "encode"),
        Input("IPv4 Output", "output")
    ]
    script = """
        const parts = data["input"].split(".")
        const res = parts.map((p) => parseInt(p, 2))
        return {
            "output": res.join(".")
        }
    """
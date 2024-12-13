from src.module import Module
from src.layout import *

class CustomModule(Module):
    name = "Base64 Decode"
    category = "encoding"
    layout = [
        Input("Base64 Input", "input", textarea=True, 
                regex=r"^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{4}|[A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{2}={2})$"),
        Submit("Submit", "encode"),
        Input("Text Output", "output", textarea=True),
    ]
    script = """return {
        "output": atob(data["input"])
    }"""
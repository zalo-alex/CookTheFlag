from src.module import Module
from src.layout import *
from src.regexs import Regexs

class CustomModule(Module):
    name = "Base64 Decode"
    category = "encoding"
    layout = [
        Input("Base64 Input", "input", textarea=True, regex=Regexs.BASE64),
        Submit("Submit", "encode"),
        Input("Text Output", "output", textarea=True),
    ]
    script = """return {
        "output": atob(data["input"])
    }"""
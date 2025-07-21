from src.module import Module
from src.layout import *
from src.regexs import RegExs

class CustomModule(Module):
    name = "Base64 Decode"
    category = "encoding"
    layout = [
        Input("Base64 Input", "input", textarea=True, regex=RegExs.BASE64),
        Submit("Submit", "encode", auto=True),
        Input("Text Output", "output", textarea=True),
    ]
    script = """return {
        "output": atob(data["input"])
    }"""
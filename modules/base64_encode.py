from src.module import Module
from src.layout import *
from src.regexs import RegExs

class CustomModule(Module):
    name = "Base64 Encode"
    category = "encoding"
    regex=RegExs.BASE64
    layout = [
        Input("Text Input", "input", textarea=True),
        Submit("Submit", "encode", auto=True),
        Input("Base64 Output", "output", textarea=True),
    ]
    script = """return {
        "output": btoa(data["input"])
    }"""
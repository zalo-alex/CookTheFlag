from src.module import Module
from src.layout import *
from src.regexs import RegExs

class CustomModule(Module):
    name = "IPv4 convert"
    category = "encoding"
    layout = [
        Input("IPv4 Input", "input", regex=RegExs.IPV4),
        Submit("Submit", "encode", auto=True),
        Input("Binary Output", "bin-output"),
        Input("Hex Output", "hex-output"),
    ]
    script = """
        var parts = data["input"].split(".")
        var bin_res = parts.map((p) => parseInt(p).toString(2)).join(".")
        var hex_res = parts.map((p) => parseInt(p).toString(16)).join(".")
        return {
            "bin-output": bin_res,
            "hex-output": hex_res
        }
    """
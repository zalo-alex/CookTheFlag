from src.module import Module
from src.layout import *

class CustomModule(Module):
    name = "URL Encode"
    category = "encoding"
    layout = [
        Input("ASCII Input", "input", textarea=True),
        CheckBox("All characters", "all_chars"),
        Submit("Submit", "encode", auto=True),
        Input("URL Encoded Output", "output", textarea=True),
    ]
    script = """
        console.log(data)
        if (data["all_chars"]) {
            return {
                "output": Array.from(data["input"]).map(char => '%' + char.charCodeAt(0).toString(16).padStart(2, '0')).join('')
            }
        }
        return {
            "output": encodeURI(data["input"])
        }
    """
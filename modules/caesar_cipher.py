from src.module import Module
from src.layout import *

class CustomModule(Module):
    name = "Caesar Cipher"
    category = "encoding"
    layout = [
        Input("Text Input", "input", textarea=True),
        Input("Rotation", "rotation", type="number"),
        Submit("Submit", "encode", auto=True),
        Input("Output", "output", textarea=True),
    ]
    script = """
        var input = data["input"]
        var rotation = parseInt(data["rotation"])
        var output = input.split('').map(char => {
            if (/[a-z]/i.test(char)) {
                const base = char === char.toUpperCase() ? 'A'.charCodeAt(0) : 'a'.charCodeAt(0);
                return String.fromCharCode((char.charCodeAt(0) - base + rotation) % 26 + base);
            }
            return char;
        }).join('');
        return {
            "output": output
        }
    """


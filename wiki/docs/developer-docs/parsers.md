# :paintbrush: Parsers

Parsers are side agnostic input data preprocessor, they can be used for server side and client side inputs, they will take the data and parse it before the module processing.

```python linenums="1"
from src.parsers import BinaryParser

class CustomModule(Module):
    layout = [
        Input("Bin Input", "input", parser=BinaryParser()),
    ]

    def submit(type, data):
        data["input"]
        # The data will be parsed for an easier processing
        # 0b1 10 --> 110
        # 01 010 --> 01010
        # 0b 011 --> 011

```

!!! warning "Page is currently in work in progress"
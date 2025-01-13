# :heavy_plus_sign: Modules

Here's a basic model of what a module is

```python title="modules/hello.py" linenums="1"
from src.module import Module
from src.layout import *

class CustomModule(Module):
    name = "Say Hello"
    category = "utils"
    layout = [
        Input("Your name", "name-input"),
        Submit("Say", "say"),
        Input("Response", "response")
    ]
    
    def submit(type, data):
        return {
            "response": "Hello " + data["name-input"]
        }
```

!!! warning "Page is currently in work in progress"
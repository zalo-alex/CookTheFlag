# :heavy_plus_sign: Modules

Here's a basic model of what a module is

```python title="modules/hello.py" linenums="1"
from src.module import Module
from src.layout import *

class CustomModule(Module):
    name = "Say Hello"
    category = "random-utils"
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

`category`
> Should be in lowercase with '-' instead of spaces

`layout`
> A list of Layout elements, the `Submit` will trigger the `submit` function with his type (here `say`)

`submit(type, data)`
> `type` is the type of the submitter  
> `data` a dict with all the contents of the inputs, the key is the ID of the element  
> It returns a dict with each content to change, element ID and value. There are no timeouts

## Client side

By adding a `script` attribute to `CustomModule` you can make your module client side.  
You will have to make it in JavaScript, the `type` and `data` are already initialized, no need to create a function

```python linenums="1"
from src.module import Module
from src.layout import *

class CustomModule(Module):
    ...
    
    script = """return {
        "response": "Hello " + data["name-input"]
    }"""
```

## Module RegEx

With the `regex` you can specify an expression for the module and not only to an input.  
It can be usefull if the user want to know the type of string he's searching.  
For more info about RegEx see [:hash: RegEx](./regex.md)

```python linenums="1"
from src.regexs import Regexs

class CustomModule(Module):
    name = "Base64 Encode"
    category = "encoding"
    regex=Regexs.BASE64
```

## Streaming response

I you need modify multiple times your response, for exemple with CLI, you can use `yield` instead of `return`

```python linenums="1"
class CustomModule(Module):
    ...
    
    def submit(type, data):
        for i in range(10):
            yield {
                "result": i
            }
            time.sleep(1)
```

!!! warning "Page is currently in work in progress"
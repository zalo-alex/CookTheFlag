# :mag: RegEx

RegEx allow users to find the right module easily, when going to the home you have a search box that will return you modules by RegEx matching.  

To specify a RegEx you can either use `re.compile` or use premade RegExs inside `src/regexs.py`

## Module scoped

This will help the user to have an idea of what the data he have could be. In this case, if the user search for `0x123` the "Hex to Binary" will show.

```python linenums="1"
from src.regexs import RegExs

class CustomModule(Module):
    name = "Hex to Binary"
    regex = re.compile(r"^(0x)?[0-9a-fA-F]+(?:\s[0-9a-fA-F]+)*$")
```

## Input scoped

Input scoped RegEx, is more powerfull than Module scoped since it automaticly fill the input for the user.  
This example use the premade RegEx, which in this case is equivalent to `re.compile(r"^(0b)?[01]+(?:\s[01]+)*$")`

```python title="modules/hello.py" linenums="1"
from src.regexs import RegExs

class CustomModule(Module):
    [...]
    layout = [
        Input("Binary Input", "input", regex=RegExs.BIN)
    ]
```

!!! warning "Page is currently in work in progress"
# :straight_ruler: Layout

## Input

``` python linenums="1"
Input(name, id, type="text", placeholder="", value="", textarea=False, regex = r"", parser = None)
```

This element is a `<input>` in HTML.

`name`
> The label, only visual

`id`
> The actual ID to retrieve and edit values

`type`, `placeholder`, `value`
> Same as HTML

`textarea`
> If true it will use a `<textarea>` instead of an `<input>`

`regex`
> The RegEx that will redirect to the input when a search is done

`parser`
> More infos [:paintbrush: Parsers](./parsers.md)

## Submit

``` python linenums="1"
Button(name, id, auto=False)
```

The button to submit the data

`name`
> The label, only visual

`id`
> The type in the submit function

`auto`
> Only for client side, will execute submit every an input is modified

!!! warning "Page is currently in work in progress"
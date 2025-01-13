# :open_file_folder: File Structure

Here are the important files if you want to create modules:
```
.
├─ modules/
└─ src/
   ├─ layout/
   ├─ parsers/
   └─ regexs.py
```

## `modules/`

This folder contains all the modules that will be loaded, you cannot use subfolders.

## `src/layout/`

This folder contains all the graphic elements that can be used in the modules. All the elements should be in the `__all__` of `__init__.py`.

## `src/parsers/`

This folder contains all the parsers that can be used in the modules, all the elements are in the `__all__` of `__init__.py`.

## `src/regexs.py`

This file contains all the regexes that can be used in the modules.

!!! warning "Page is currently in work in progress"
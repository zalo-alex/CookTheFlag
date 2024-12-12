from src.layout.element import Element

class KeyValue(Element):
    element_type = "key_value"
    
    def __init__(self, name, id, default={}):
        self.name = name
        self.id = id
        self.default = default
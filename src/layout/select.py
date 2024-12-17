from src.layout.element import Element

class Select(Element):
    element_type = "select"
    
    def __init__(self, name, id, options=[]):
        self.name = name
        self.id = id
        self.options = options
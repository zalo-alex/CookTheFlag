from src.layout.element import Element

class Select(Element):
    element_type = "select"
    
    def __init__(self, name, id, options=[]):
        self.name = name
        self.id = id
        self.options = zip(options, options if type(options) == list else options.values())
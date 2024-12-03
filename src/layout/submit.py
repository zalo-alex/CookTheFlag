from src.layout.element import Element

class Submit(Element):
    element_type = "submit"
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
from src.layout.element import Element

class CheckBox(Element):
    element_type = "checkbox"
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
from src.layout.element import Element

class Input(Element):
    element_type = "input"
    
    def __init__(self, name, id, type="text", placeholder="", value="", textarea=False, regex = r""):
        self.name = name
        self.id = id
        self.type = type
        self.placeholder = placeholder
        self.value = value
        self.textarea = textarea
        self.regex = regex
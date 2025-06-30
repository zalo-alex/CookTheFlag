from src.layout.element import Element
from src.parsers import PathParser

class FileInput(Element):
    element_type = "file_input"
    parser = PathParser()
    
    def __init__(self, name, id, value=""):
        self.name = name
        self.id = id
        self.value = value
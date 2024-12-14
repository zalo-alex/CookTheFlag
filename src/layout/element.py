from src.parsers.parser import Parser

class Element:
    element_type: str
    regex: str = r""
    parser: Parser = None
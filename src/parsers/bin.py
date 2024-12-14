from src.parsers.parser import Parser

class BinaryParser(Parser):
    def compile(self, data):
        return data.replace("0b", "").replace(" ", "").strip()
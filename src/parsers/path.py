from src.parsers.parser import Parser

class PathParser(Parser):
    def compile(self, data):
        return data.path().strip()
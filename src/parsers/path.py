from src.parsers.parser import Parser
from src.globals import data_dir

class PathParser(Parser):
    def compile(self, data):
        return data.strip().join_path_before(data_dir).path()
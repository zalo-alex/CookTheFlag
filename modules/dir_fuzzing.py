from src.parsers.path import PathParser
from src.module import Module
from src.layout import *
from src.regexs import RegExs
from src.exec import Exec

class CustomModule(Module):
    name = "Dir Fuzzing"
    category = "tool"
    layout = [
        Input("Target URL", "url", regex=RegExs.URL),
        FileInput("Wordlist", "wordlist"),
        Submit("Fuzz", "fuzz"),
        Input("Result", "output", textarea=True),
    ]
    
    def submit(type, data):
        yield from Exec(["feroxbuster", "--url", data.get("url"), "-w", data.get("wordlist"), "-q"]).stream_output("output")
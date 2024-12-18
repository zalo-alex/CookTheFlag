from src.module import Module
from src.layout import *
from src.parsers import PathParser
from src.exec import Exec

class CustomModule(Module):
    name = "Hashcat"
    category = "tool"
    layout = [
        Input("Hash", "input"),
        Select("Mode", "mode", {
            "MD5": "0",
            "SHA1": "100",
        }),
        Input("Wordlist", "wordlist", parser=PathParser()),
        Submit("Crack", "crack"),
        Input("Command", "command"),
        Input("Result", "result"),
        Input("Output", "output", textarea=True)
    ]
    
    def submit(type, data):
        open("hash.txt", "w").write(data["input"])
        cmd = ["hashcat", "-m", data["mode"], "hash.txt", data["wordlist"]]
        yield {
            "command": " ".join(cmd)
        }
        for line in Exec(cmd).run():
            yield {
                "output": line
            }
        for line in Exec(cmd + ["--show"]).run():
            yield {
                "result": line
            }
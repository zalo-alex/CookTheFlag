from src.module import Module
from src.layout import *
from src.regexs import Regexs
from src.exec import Exec

class CustomModule(Module):
    name = "NMap"
    category = "tool"
    layout = [
        Input("Target", "input", regex=Regexs.IPV4),
        CheckBox("Service version", "version"),
        CheckBox("OS detection", "os"),
        Submit("Scan", "scan"),
        Input("Command", "command"),
        Input("Result", "output", textarea=True),
    ]
    
    def submit(type, data):
        args = []
        if data.get('version'): args.append('-sV')
        if data.get('os'): args.append('-O')
        cmd = ["nmap", *args, data['input']]
        yield {
            "command": " ".join(cmd)
        }
        for line in Exec(cmd).run():
            yield {
                "output": line
            }
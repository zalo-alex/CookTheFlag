from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit
from src.layout.select import Select

import requests

class CustomModule(Module):
    name = "Requests"
    category = "Tool"
    layout = [
        Input("URL", "url-input"),
        Select("Method", "method", ["GET", "POST"]),
        Submit("Send", "send"),
        Input("Text Response", "output", textarea=True),
    ]
    
    def submit(type, data):
        r = requests.request(data["method"], data["url-input"])
        return {
            "output": r.text
        }
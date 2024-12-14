from src.module import Module
from src.layout import *
from src.regexs import Regexs

import requests

class CustomModule(Module):
    name = "Requests"
    category = "tool"
    layout = [
        Input("URL", "url-input", regex=Regexs.URL),
        Select("Method", "method", ["GET", "POST"]),
        KeyValue("Headers", "headers"),
        Submit("Send", "send"),
        Input("Text Response", "output", textarea=True),
    ]
    
    def submit(type, data):
        r = requests.request(data["method"], data["url-input"], headers=data["headers"])
        return {
            "output": r.text
        }
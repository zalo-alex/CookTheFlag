from src.module import Module
from src.layout.input import Input
from src.layout.submit import Submit
from src.layout.select import Select
from src.layout.key_value import KeyValue

import requests

class CustomModule(Module):
    name = "Requests"
    category = "Tool"
    layout = [
        Input("URL", "url-input", regex=r"^https?:\/\/([A-Za-z0-9.-]+)(:[0-9]{1,5})?(\/[^\s]*)?$"),
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
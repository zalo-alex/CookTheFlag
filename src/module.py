class Module:
    
    name: str
    category: str
    layout: list
    regex: str = r""
    script: str = None
    
    def submit(type: str, data: dict):
        pass
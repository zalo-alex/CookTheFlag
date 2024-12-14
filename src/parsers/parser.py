from src.parsers.actions import ActionDummy, Action

class Parser:
    
    def __init__(self):
        self.actions: list[Action] = []
        self.is_client_side = False
    
    def _compile(self):
        self.actions = self.compile(ActionDummy()).actions
    
    def compile(self, data: ActionDummy):
        return data
    
    def parse(self, data):
        """ Server side parsing """
        for action in self.actions:
            data = action.run(data)
        return data
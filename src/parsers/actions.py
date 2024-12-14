from __future__ import annotations

from pathlib import Path

class Action:
    def __init__(self, name, options, process, script=None):
        self.name = name
        self.options = options
        self.process = process
        self.script = script
    
    def run(self, data):
        """ Server side run action """
        return self.process(data, self.options)

    def is_client_side(self):
        return bool(self.script)

def action_wrapper(func):
    def wrapper(self, *args, **kwargs):
        action = func(self, *args, **kwargs)
        self.actions.append(action)
        self.is_client_side = max(self.is_client_side, action.is_client_side())
        return self
    return wrapper

class ActionDummy:
    
    def __init__(self):
        self.actions: list[Action] = []
        self.is_client_side = False
    
    @action_wrapper
    def replace(self, old, new) -> ActionDummy:
        def process(data, options):
            return data.replace(options["old"], options["new"])
        
        return Action(
            "replace", 
            {
                "old": old,
                "new": new
            },
            process,
            """data = data.replaceAll(options.old, options.new)"""
        )
    
    @action_wrapper
    def strip(self) -> ActionDummy:
        def process(data, options):
            return data.strip()
        
        return Action(
            "strip", 
            {},
            process,
            """data = data.trim()"""
        )
    
    @action_wrapper
    def path(self) -> ActionDummy:
        def process(data, options):
            return Path(data).resolve().as_posix()
        
        return Action(
            "path", 
            {},
            process
        )
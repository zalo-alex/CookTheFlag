import subprocess

class Exec:
    
    def __init__(self, args):
        self.args = args
    
    def run(self):
        return subprocess.run([*self.args], capture_output=True, text=True).stdout
import subprocess

class Exec:
    
    def __init__(self, process, args):
        self.process = process
        self.args = args
    
    def run(self):
        return subprocess.run([self.process, *self.args], capture_output=True, text=True).stdout
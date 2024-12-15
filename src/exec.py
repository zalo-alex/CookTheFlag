import subprocess

class Exec:
    
    def __init__(self, args):
        self.args = args
    
    def run(self):
        process = subprocess.Popen([*self.args], stdout=subprocess.PIPE)
        total = b""
        for stdout_line in iter(process.stdout.readline, b''):
            total += stdout_line
            yield total.decode("latin-1")
import threading
import uuid
import json

from src.websocket import broadcast

class Task:
    name = "Undefined"

    def __init__(self):
        """Pre run execution, can throw an exception"""
        self.id = str(uuid.uuid4())

    def run(self):
        """Run the task, ran in a separate thread"""

    def cleanup(self):
        """Post run or cancel cleanup"""

class Tasks:

    all: dict[str, Task] = {}

    @classmethod
    def start(cls, task: Task):
        cls.all[task.id] = task
        threading.Thread(target=task.run).start()
        cls.broadcast_amount()

    @classmethod
    def stop(cls, task: Task):
        cls.all[task.id].cleanup()
        del cls.all[task.id]
        cls.broadcast_amount()
    
    @classmethod
    def amount(cls):
        return len(cls.all)

    @classmethod
    def broadcast_amount(cls):
        broadcast(json.dumps({
            "type": "running_tasks",
            "data": {
                "amount": cls.amount()
            }
        }))
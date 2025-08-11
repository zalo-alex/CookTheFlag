# :man_running_tone1: Tasks

To create background task you can use `Task` and `Tasks` class. A task have 3 methods, the `__init__()` which can throw an error if you need for error handling, then `run()` that's ran in a thread, and `cleanup()` to end the task.

```python title="src/tasks.py" linenums="1"
class Task:
    name = "Undefined"

    def __init__(self):
        """Pre run execution, can throw an exception"""
        self.id = str(uuid.uuid4())

    def run(self):
        """Run the task, ran in a separate thread"""

    def cleanup(self):
        """Post run or cancel cleanup"""
```

## Usage example

```python title="modules/test_tasks.py" linenums="1"
[...]
from src.tasks import Task, Tasks

class MyTask(Task):
    name = "My Task"
    
    def __init__(self, name):
        super().__init__()
        self.running = True
        self.name = name
        print("My task is initialized!")
    
    def run(self):
        while self.running:
            print(f"Hello {self.name}")
            time.sleep(1)
    
    def cleanup(self):
        self.running = False

class CustomModule(Module):
    [...]
    
    def submit(type, data):
        task = MyTask(data.get("name"))
        Tasks.start(task)
```

> See `modules/http_exploit_server.py` for an other example

!!! warning "Page is currently in work in progress"
import os
from pathlib import Path

data_dir = "/data" if os.getenv("DOCKER") else os.path.join(Path.home(), ".cooktheflag")
print("DATA DIR:", data_dir)
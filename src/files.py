import os
import shutil
from pathlib import Path

class DownloadableFile:
    
    def __init__(self, url):
        self.url = url

class Files:

    structure = {
        "wordlists": {
            "10-million-password-list-top-100000.txt": DownloadableFile("https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt")
        }
    }

    def __init__(self):
        self.data_dir = "/data" if os.getenv("DOCKER") else os.path.join(Path.home(), ".cooktheflag")
        self.init_folders(self.data_dir, self.structure)

    def get_absolute_path(self, path):
        return os.path.join(self.data_dir, self.get_path(path))
    
    def get_path(self, path):
        return os.path.relpath(os.path.normpath(os.path.join("/", path)), "/")

    def init_folders(self, path, sub):
        for folder in sub:
            if type(sub[folder]) == dict:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)
                self.init_folders(folder_path, sub[folder])
    
    def exists(self, path):
        return os.path.exists(self.get_absolute_path(path))

    def structure_from_path(self, path):
        parts = path.split("/")
        sub = self.structure
        for part in parts:
            if part not in sub:
                return {}
            sub = sub[part]
        return sub

    def get_downloadables(self, path):
        downloadables = []
        strct = self.structure_from_path(path)
        for file in strct:
            if type(strct[file]) == DownloadableFile:
                downloadables.append(file)
        return downloadables

    def list_dir(self, path):
        abs_path = self.get_absolute_path(path)
        folders = []
        files = []
        for file in os.listdir(abs_path):
            p = os.path.join(abs_path, file)
            if os.path.isdir(p):
                folders.append(file)
            else:
                files.append(file)
        return folders, files

    def save_file(self, path, file):
        file.save(os.path.join(self.get_absolute_path(path), file.filename))
    
    def delete_file(self, path):
        path = self.get_absolute_path(path)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
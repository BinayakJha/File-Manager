
import os
from rich.progress import track


def find_folders(filename, search_path):
    return [
        os.path.join(root, filename)
        for root, dir, files in os.walk(search_path)
        if filename in dir
    ]

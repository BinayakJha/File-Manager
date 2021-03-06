
import os
def find_folders(filename, search_path):
    print('Searching for {} in {}'.format(filename, search_path))
    return [
        os.path.join(root, filename)
        for root, dir, files in os.walk(search_path)
        if filename in dir
    ]

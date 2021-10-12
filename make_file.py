import os
import shutil
def make_files(file11,folder,name,file1):
    if not os.path.isdir(os.path.join(folder, name)):
        os.mkdir(os.path.join(folder,name))

    shutil.move(file11, folder+"/"+name+"/"+file1)
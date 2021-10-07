

# installing dependicies
print("Checking If packages are installed or not")
try:
    from inspect import trace
    import os
    import shutil
    from rich import console
    from rich import syntax
    import find_file
    from time import sleep
    # rich library
    from rich import print
    from rich.console import Console
    from rich.text import Text
    from rich.progress import track
    from rich.prompt import Prompt
    # traceback error
    from rich.traceback import install
    from rich.markdown import Markdown
except ImportError:
    ask = input('''Packages Not Found.
    Would you like to install them? (y/n)''')
    if ask == 'y':
        print('\n')
        print('Checking if pip is installed or not')
        os.system('python -m pip install --upgrade pip')
        print("Installing packages .......")
        print("""
 ____  ___ ____ _   _ 
|  _ \|_ _/ ___| | | |
| |_) || | |   | |_| |
|  _ < | | |___|  _  |
|_| \_\___\____|_| |_|
        """)
        os.system('pip install rich')
        os.system('pip install requests')
        print("Packages installed :)")# console
        print("Checking If packages are installed or not")
        try:
            from inspect import trace
            import os
            import shutil
            from rich import console
            from rich import syntax
            import find_file
            from time import sleep
            # rich library
            from rich import print
            from rich.console import Console
            from rich.text import Text
            from rich.progress import track
            from rich.prompt import Prompt
            # traceback error
            from rich.traceback import install
            from rich.markdown import Markdown
        except ImportError:
            print("Sorry some error  occured while installing Packages \n Try installing manually")
            print("Exiting")
            exit()
    os.system("cls" if os.name == "nt" else "clear")
console = Console()
os.system("cls" if os.name == "nt" else "clear")
install()
# markdown

MARKDOWN = """
# FILE MANAGER                     
## **Made By:** BinayakJha
"""
md = Markdown(MARKDOWN)
console.print(md)
image_formats = ["jpg", "jpeg", "png", "gif", "bmp"]
video_formats = ["mp4", "mkv", "avi", "flv", "wmv", "mov"]
audio_formats = ["mp3", "wav", "aac", "ogg", "flac", "mp4"]
docs_formats = ["ai", "ait", "txt", "rtf"]

python_format = ["py", "pyc", "pyw", "pyo", "pyi"]
jupyter_format = ["ipynb"]
c_format = ["c", "cpp"]
java_format = ["java"]
input = Text("Enter the folder name you want to manage: (Case sensitive) ")
input.stylize("bold blue")
console.print(input)

# folder_input = console.input("=>")
folder_input = console.input("=>")
# finding files
if os.name == "nt":
    folder = find_file.find_folders(folder_input,"C:\\")
else:
    folder = find_file.find_folders(folder_input,"/Users/")[0]
print(folder)

# functions
def init():
    if not os.path.isdir(os.path.join(folder,"python files")):
        os.mkdir(os.path.join(folder,"python files"))
    if not os.path.isdir(os.path.join(folder,"jupyter files")):
        os.mkdir(os.path.join(folder,"jupyter files"))
    if not os.path.isdir(os.path.join(folder,"c files")):
        os.mkdir(os.path.join(folder,"c files"))
    if not os.path.isdir(os.path.join(folder,"java files")):
        os.mkdir(os.path.join(folder,"java files"))
    
init()
while True:
    console.print("Started :thumbs_up:", style="bold green")
    sleep(3)
    files = os.listdir(folder)
    for file in track(files, description="Processing......"):
        ext = (file.split(".")[-1]).lower()
        file11 = os.path.join(folder,file)
        if ext in image_formats:
            shutil.move(file11, "images/"+file)
        elif ext in audio_formats:
            shutil.move(file11, "audio/"+file)
        elif ext in video_formats:
            shutil.move(file11, "videos/"+file)
        elif ext in docs_formats:
            shutil.move(file11, "docs/"+file)
            console
        elif ext in python_format:
            shutil.move(file11, folder+"/python files/"+file)
        elif ext in jupyter_format:
            shutil.move(file11, folder+"/jupyter files/"+file)
        elif ext in c_format:
            shutil.move(file11, folder+"/c files/"+file)
        elif ext in java_format:
            shutil.move(file11, folder+"/java files/"+file)
        sleep(0.1)
    console.print("File moved :thumbs_up:", style="bold red")
    del files  # if program is using too much memory increae the value of sleep function
    sleep(5)

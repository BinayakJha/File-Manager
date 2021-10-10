
# installing dependicies

try:

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
        from rich import style
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
            print("Packages installed :)")  # console
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
                from rich import style
            except ImportError:
                print(
                    "Sorry some error  occured while installing Packages \n Try installing manually")
                print("Exiting")
                exit()
        os.system("cls" if os.name == "nt" else "clear")
    console = Console()
    os.system("cls" if os.name == "nt" else "clear")
    install()
    # markdown

    MARKDOWN = """
# FILE MANAGER   **VERSION 1.0**                  
## **Made By:** BinayakJha
##

    """
    md = Markdown(MARKDOWN)
    console.print(md)
    # formats of the files
    # videos and other common files
    image_formats = ["tif", "tiff", "bmp", "jpg", "jpeg",
                     "gif", "png", "eps", "raw", "cr2", "nef", "orf", "sr2"]
    video_formats = ["mp4", "mov", "wmv", "flv", "avi", "avchd", "webm", "mkv"]
    audio_formats = ["mp3", "wav", "aac", "ogg",
                     "flac", "mp4", "3gp", "aa", "aac", "aax", "wma"]
    docs_formats = ["ai", "ait", "txt", "rtf",
                    "doc", "pdf", "ods", "docx", "csv", "xlsx"]
    presentational_formats = ["ppt", "pptx", "key", "keynote", "odp", "pot", "potx", "pps", "ppsx", "pptm", "ppsm", "sldx", "sldm", "odp",
                              "pot", "potx", "pps", "ppsx", "ppt", "pptx", "key", "keynote", "odp", "pot", "potx", "pps", "ppsx", "pptm", "ppsm", "sldx", "sldm"]
    # programming language files
    html_formats = ["html", "htm", "xhtml"]
    css_formats = ["css"]
    javascript_formats = ["js"]
    python_format = ["py", "pyc", "pyw", "pyo", "pyi"]
    jupyter_format = ["ipynb"]
    c_format = ["c", "cpp"]
    java_format = ["java"]
    # format of file end
    input = Text("Enter the folder name you want to manage: (Case sensitive) ")
    input.stylize("bold blue")
    input.stylize("bold red", 41, 58)
    console.print(input)
    # FOLDER NAME INPUT
    folder_input = console.input("=>")
    # ask for run as admnistrator permission to access the folder
    # finding files
    if os.name == "nt":
        try:
            folder = find_file.find_folders(
                folder_input, "C:\\Users\\" + os.getlogin()+"\\")[0]
        except IndexError:
            console.print("Folder Not Found", style="bold red")
            sleep(1)
            console.print("RESTARTING....", style="bold green")
            sleep(1)
            os.system("cls")
            os.system("python main.py")

    else:
        try:
            folder = find_file.find_folders(folder_input, "/Users/")[0]
        except IndexError:
            console.print("\n Folder Not Found", style="bold red")
            sleep(1)
            console.print("\n RESTARTING....", style="bold green")
            sleep(0.5)
            os.system("clear")
            os.system("python main.py")
    print(folder)

    # functions
    while True:
        console.print("Started :thumbs_up:", style="bold green")
        sleep(3)
        files = os.listdir(folder)
        for file in track(files, description="Processing......"):
            ext = (file.split(".")[-1]).lower()
            file11 = os.path.join(folder, file)

            if ext in image_formats:
                # making the folder only if it is not present
                if not os.path.isdir(os.path.join(folder, "Images")) or not os.path.isdir(os.path.join(folder, "images")):
                    os.mkdir(os.path.join(folder, "Images"))

                shutil.move(file11, folder+"/Images/"+file)

            elif ext in audio_formats:
                # making the folder only if it is not present
                if not os.path.isdir(os.path.join(folder, "Audio")):
                    os.mkdir(os.path.join(folder, "Audio"))

                shutil.move(file11, folder+"/Audio/"+file)

            elif ext in video_formats:
                # making the folder only if it is not present
                if not os.path.isdir(os.path.join(folder, "Video")) or not os.path.isdir(os.path.join(folder, "video")) or not os.path.isdir(os.path.join(folder, "Videos")) or not os.path.isdir(os.path.join(folder, "videos")):
                    os.mkdir(os.path.join(folder, "Videos"))

                shutil.move(file11, folder+"/Videos/"+file)

            elif ext in docs_formats:
                # making the folder only if it is not present
                if not os.path.isdir(os.path.join(folder, "Documents")):
                    os.mkdir(os.path.join(folder, "Documents"))

                shutil.move(file11, folder+"/Documents/"+file)

            elif ext in presentational_formats:
                if not os.path.isdir(os.path.join(folder, "Documents/Presentation")):
                    os.mkdir(os.path.join(folder, "Documents/Presentation"))

                shutil.move(file11, folder+"/Documents/Presentation/"+file)
            # programming files
            elif ext in html_formats:
                if not os.path.isdir(os.path.join(folder, "HTML")):
                    os.mkdir(os.path.join(folder, "HTML"))

                shutil.move(file11, folder+"/HTML/"+file)
            elif ext in css_formats:
                if not os.path.isdir(os.path.join(folder, "CSS")):
                    os.mkdir(os.path.join(folder, "CSS"))

                shutil.move(file11, folder+"/CSS/"+file)
            elif ext in javascript_formats:
                if not os.path.isdir(os.path.join(folder, "JavaScript")):
                    os.mkdir(os.path.join(folder, "JavaScript"))

                shutil.move(file11, folder+"/JavaScript/"+file)

            elif ext in python_format:
                # making the folder only if it is not present
                if not os.path.isdir(os.path.join(folder, "python files")):
                    os.mkdir(os.path.join(folder, "python files"))

                shutil.move(file11, folder+"/python files/"+file)

            elif ext in jupyter_format:
                # making the folder only if it is not present
                if not os.path.isdir(os.path.join(folder, "jupyter files")):
                    os.mkdir(os.path.join(folder, "jupyter files"))

                shutil.move(file11, folder+"/jupyter files/"+file)

            elif ext in c_format:
                # making the folder only if it is not present
                if not os.path.isdir(os.path.join(folder, "c files")):
                    os.mkdir(os.path.join(folder, "c files"))

                shutil.move(file11, folder+"/c files/"+file)

            elif ext in java_format:
                # making the folder only if it is not present
                if not os.path.isdir(os.path.join(folder, "java files")):
                    os.mkdir(os.path.join(folder, "java files"))

                shutil.move(file11, folder+"/java files/"+file)

            sleep(0.1)
        console.print("File moved :thumbs_up:", style="bold red")
        console.print("Press Ctrl+c to end the program", style="bold blue")
        del files  # if program is using too much memory increae the value of sleep function
        sleep(5)
except KeyboardInterrupt:
    console.print("\nExiting....", style="bold red")
    sleep(1)
    console.print("\nBye Bye and thanks for using this app",
                  style="bold green")
    sleep(1)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    os.system("exit")

import os
import time
import json
from Sources.mainSource import MAIN_SOURCE_CODE
from Sources.pingSource import PING_SOURCE_CODE
from Sources._colorsSource import COLORS_SOURCE_CODE
from Sources.configSource import CONFIG_SOURCE_CODE
from Sources.functionsSource import FUNCTIONS_SOURCE_CODE

class Colors:
    def __init__(self) -> None:
        self.RED = "\033[31m"
        self.GREEN = "\033[32m"
        self.YELLOW = "\033[33m"
        self.BLUE = "\033[34m"
        self.MAGENTA = "\033[35m"
        self.CYAN = "\033[36m"
        self.WHITE = "\033[37m"
        self.RESET = "\033[0m"  

class FolderInit:
    def __init__(self) -> None:
        self.pythonFiles = ['functions', 'main', "_colors"]
        self.jsonFiles = ['config']
        self.folders = ['commands', 'events', 'views']
        self.C = Colors()

    def create_py_files(self) -> None:
        for filename in self.pythonFiles:
            with open(f"{filename}.py", 'w') as f:
                if filename == "main":
                    f.write(MAIN_SOURCE_CODE)
                elif filename == "_colors":
                    f.write(COLORS_SOURCE_CODE)
                elif filename == "functions":
                    f.write(FUNCTIONS_SOURCE_CODE)
                f.close()
            print(f"{self.C.GREEN}[SUCCESS] {self.C.WHITE} ./{filename}.py created !")

    def create_exemple_command(self) -> None:
        os.mkdir('./commands/utils')
        with open("./commands/utils/exemple.py", "w") as f:
            f.write(PING_SOURCE_CODE)
            f.close()        
        print(f"{self.C.GREEN}[SUCCESS] {self.C.WHITE} ./commands/utils/exemple.py created !")

    def create_json_file(self) -> None:
        for filename in self.jsonFiles:
            with open(f"{filename}.json", 'w') as f:
                if filename == "config":
                    f.write(CONFIG_SOURCE_CODE)
                else:
                    f.write("{}")
                f.close()
            print(f"{self.C.GREEN}[SUCCESS] {self.C.WHITE} ./{filename}.json created !")

    def create_folders(self) -> None:
        for folder in self.folders:
            os.mkdir(folder)
            print(f"{self.C.GREEN}[SUCCESS] {self.C.WHITE} ./{folder}/ created !")

    def input_token(self, token) -> None:
        config = json.load(open("config.json", 'r'))
        config['token'] = token
        print(f"{self.C.GREEN}[UPDATING] {self.C.WHITE} Dumping json file...")
        json.dump(config, open("config.json", 'w'), indent=4)
        print(f"{self.C.GREEN}[SUCCESS] {self.C.WHITE} Bot token update into ./config.json")

    def main(self) -> None:
        now = time.time()
        self.create_py_files()
        self.create_json_file()
        self.create_folders()
        self.create_exemple_command()
        choice = input(f"{self.C.RED}[INPUT] {self.C.WHITE} Auto change bot token (y/n) ?: ")
        token = input(f"{self.C.RED}[INPUT] {self.C.WHITE} Enter Bot Token: ")
        elaspedTime = time.time() - now
        print(f'{self.C.BLUE}[INFO] {self.C.WHITE} Finished in {elaspedTime:.2} seconds.')
        if choice == "y" or choice == "yes":
            self.input_token(token)
            choice = input(f"{self.C.RED}[INPUT] {self.C.WHITE} Start Bot (y/n) ?: ")
            if choice == "yes" or choice == "y":
                os.system('python main.py')

Init = FolderInit()
Init.main()
import os
import csv

commands = {
    "help": "Show help",
    "add": "Add new project or shot",
    "conf": "Configure software list",
    "list": "List all project",
    "go": "Run software with selected project and shot",
    "clear": "Clear the command line",
    "reload": "Reload scripts",
    "reset": "Reset work environment",
    "exit": "Close PyPline",
}



file = os.path.abspath("config.csv")
if os.path.isfile(file):
    with open(file, mode="r", encoding="UTF-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        soft = {i["software"]: {"path": i["path"], "ext":i["extension"], "matrice":i["matrices"]} for i in csv_reader if i["path"] != "#    Path not Defined    #"}


        
commands.update({i: f"Execute le programme {i}" for i in soft})
print(commands)
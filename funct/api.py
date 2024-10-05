import csv
import os
import subprocess as sp

# from rich import print

from funct.frame import create_frame


class API:

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
    software_paths = {}
    software_ext = {}
    help = []
    software_dict = []

    file = os.path.abspath("config.csv")
    if os.path.isfile(file):
        with open(file, mode="r", encoding="UTF-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            soft = {i["software"]: {"path": i["path"], "ext":i["extension"], "matrice":i["matrices"]} for i in csv_reader if i["path"] != "#    Path not Defined    #"}

    else:
        create_frame(["config.csv missing", "new config.csv file created"])
        data = ["software", "path", "matrices", "extension"]
        with open(file, mode="w", newline="", encoding="UTF-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)

    commands.update({i: f"Execute le programme {i}" for i in soft})


def commandList():
    return API.commands


def showHelp():
    create_frame([f"   {i}: {API.commands[i]}    " for i in API.commands])
    #print([f"   {i}: {API.commands[i]}    " for i in API.commands])


def testHelp(soft):
    if soft in API.software_dict:
        sp.Popen(API.software_paths[soft])
        # print(f"{soft} : {ConfigCSV.software_paths[soft]}")

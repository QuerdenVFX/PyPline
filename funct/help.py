import csv
from rich import print
from funct.frame import create_frame
import os
import subprocess as sp


class API():
    
        commands = {
        "help": "Show help",
        "add": "Add new project or shot",
        "conf": "Configure software list",
        "list": "List all project",
        "go": "Run software with selected project and shot", 
        "clear": "Clear the command line",
        "reload": "Reload scripts",
        "reset":"Reset work environment",
        "exit": "Close PyPline"
    }
        software_paths = {}
        software_ext = {}
        help = []
        software_dict = []


        file = os.path.abspath("config.csv")
        if os.path.isfile(file):
            with open(file, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if row["path"] != "#    Path not Defined    #":
                        software = row['software']
                        commands[software] = f"Execute le programme {software}"
                        software_paths[software] = row["path"]
                        software_dict.append(software)
                        software_ext[software] = row["extension"]

        else:
            create_frame(['config.csv missing', 'new config.csv file created'])
            data = ['software','path','matrices','extension']
            with open(file, mode="w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(data)

        for command, description in commands.items():
                help.append(f"   {command}: {description}    ")


def commandList():
    return API.commands



def showHelp():
    create_frame(API.help, center=False)


def testHelp(soft):
     if soft in API.software_dict:
        sp.Popen(API.software_paths[soft])
          #print(f"{soft} : {ConfigCSV.software_paths[soft]}")
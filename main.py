import csv
import glob
import importlib
import json as jsw
import os
import shutil
import subprocess as sp
import tkinter as tk
import xml.etree.ElementTree as ET
from pathlib import Path
from tkinter import Button, filedialog, messagebox, ttk

import pandas as pd
from InquirerPy import get_style, inquirer
from InquirerPy.base.control import Choice
from rich import print
from rich.console import Console
from rich.table import Table
from rich.tree import Tree

import funct.add as fAdd
import funct.config as fConf
import funct.frame as fFrame
import funct.help as fHelp
import funct.list as fList

# Importation des modules de ton package
import funct.open as fOpen
import funct.setEnv as fSet
import funct.styleInquirer as fStyle


def ask():
    ask = inquirer.text(
        message=">",
        completer={i: None for i in fHelp.commandList()},
        style=fStyle.Style(),
    ).execute()
    cmd = ask.split(" ")
    if cmd[0] == "go":
        go(cmd)
    elif cmd[0] in fHelp.API.software_dict:
        fSet.remove()
        sp.Popen(fHelp.API.software_paths[cmd[0]])
    else:
        exec(f"{cmd[0]}()")


def reload():
    importlib.reload(fOpen)
    importlib.reload(fAdd)
    importlib.reload(fConf)
    importlib.reload(fList)
    importlib.reload(fHelp)
    importlib.reload(fFrame)
    importlib.reload(fSet)
    print("All script reloaded")


def help():
    fHelp.showHelp()


def add():
    fAdd.add()


def conf():
    fConf.conf()


def go(inp):
    fOpen.openShot(inp)


def list():
    fList.listShot()


def clear():
    if os.name == "nt":  # Pour Windows
        os.system("cls")
    else:  # Pour macOS et Linux (systèmes Unix-based)
        os.system("clear")


def reset():
    fSet.remove()


class CLI:
    def run(self):
        print("\nWelcome in PyPline\n")
        while True:
            try:
                ask()
            except NameError:
                print("Command not valid.\nChose commande existing in command list: \n")
                help()
            except Exception as e:
                print(f"An error occured: {e}")


try:
    cli = CLI()
    cli.run()
except KeyboardInterrupt:
    print("CLOSE PYPLINE")

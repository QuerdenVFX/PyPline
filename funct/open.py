import glob
import os
import csv
import subprocess as sp
import funct.setEnv as setEnv
from rich.table import Table
from rich.console import Console
import json as js
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from funct.frame import create_frame
from funct.help import API as api

def frame(project, shot, software):
    shot_data_path = f'./PROJECT DIRECTORY/{project}/{shot}/_Library/{shot}_data.json'

    with open(shot_data_path, mode="r") as json:
        data= js.load(json)
        resolution = f'{data["ResolutionX"]}x{data["ResolutionY"]}'
        framerate = data["FrameRate"]


    table = Table()
    table.add_column("Project")
    table.add_column("Shot")
    table.add_column("Resolution")
    table.add_column("Frame Rate")
    table.add_column("Software")
    

    table.add_row(project, shot, resolution, str(framerate), software)
    console= Console()
    console.print(table)


def openShot(input):
    try:
            if input == ["go"]:
                dir = os.path.abspath("./PROJECT DIRECTORY")
                proj_list = os.listdir(dir)
                
                project_sel = inquirer.select(message="Project :", choices=proj_list).execute()

                shot_list = os.listdir(f"{dir}/{project_sel}")
                shot_list.remove("ShotList.json")

                shot_sel = inquirer.select(message="Shot :", choices=shot_list).execute()
                    
                soft_list = os.listdir(f"{dir}/{project_sel}/{shot_sel}/")
                soft_list.remove("_Library")
                
                soft_sel = inquirer.select(message="Software :", choices=soft_list).execute().lower()
                    

            else:
                project_sel = input[1]
                shot_sel = input[2]
                soft_sel = input[3]

            if soft_sel in api.software_paths:
                 soft_ext = api.software_ext[soft_sel]
                 path = api.software_paths[soft_sel]          


            directory = f'./PROJECT DIRECTORY/{project_sel}/{shot_sel}/{soft_sel}/'
            pattern = os.path.join(directory, f"{shot_sel}_v[0-9][0-9][0-9].{soft_ext}")
            version = len(glob.glob(pattern))

            file = f'{directory}/{shot_sel}_v{version:03}.{soft_ext}'

            setEnv.set(shot_sel)

            sp.Popen([path, os.path.abspath(file)])



            frame(project_sel, shot_sel, soft_sel)
    except IndexError:
        error: str = ["La fonction a besoin de 3 arguments", "SHOW SHOT SOFTWARE", 'ex: go test tes houdini']
        create_frame(error, center= True)
        print(input)
import glob
import json as js
import os
import subprocess as sp

from InquirerPy import inquirer
from rich.console import Console
from rich.table import Table

import funct.setEnv as setEnv
from funct.api import API as api
from funct.frame import create_frame


def frame(project, shot, software):
    """Function for displaying shot information"""
    shot_data_path = f"./PROJECT DIRECTORY/{project}/{shot}/_Library/{shot}_data.json"

    with open(shot_data_path, mode="r", encoding="UTF-8") as json:
        data = js.load(json)
        resolution = f'{data["ResolutionX"]}x{data["ResolutionY"]}'
        framerate = data["FrameRate"]

    table = Table()
    table.add_column("Project")
    table.add_column("Shot")
    table.add_column("Resolution")
    table.add_column("Frame Rate")
    table.add_column("Software")

    table.add_row(project, shot, resolution, str(framerate), software)
    console = Console()
    console.print(table)


def open_shot(cmds):
    """Function for opening shot"""
    try:
        if cmds == ["go"]:
            dir_proj = os.path.abspath("./PROJECT DIRECTORY")
            proj_list = os.listdir(dir_proj)

            project_sel = inquirer.select(
                message="Project :", choices=proj_list
            ).execute()

            shot_list = os.listdir(f"{dir_proj}/{project_sel}")
            shot_list.remove("ShotList.json")

            shot_sel = inquirer.select(message="Shot :", choices=shot_list).execute()

            soft_list = os.listdir(f"{dir_proj}/{project_sel}/{shot_sel}/")
            soft_list.remove("_Library")

            soft_sel = (
                inquirer.select(message="Software :", choices=soft_list)
                .execute()
                .lower()
            )

        else:
            project_sel = cmds[1]
            shot_sel = cmds[2]
            soft_sel = cmds[3]

        if soft_sel in api.soft:
            soft_ext = api.soft[soft_sel]["ext"]
            path = api.soft[soft_sel]["path"]

        directory = f"./PROJECT DIRECTORY/{project_sel}/{shot_sel}/{soft_sel}/"
        pattern = os.path.join(directory, f"{shot_sel}_v[0-9][0-9][0-9].{soft_ext}")
        version = len(glob.glob(pattern))

        file = f"{directory}/{shot_sel}_v{version:03}.{soft_ext}"

        setEnv.set_env(shot_sel)

        sp.Popen([path, os.path.abspath(file)])

        frame(project_sel, shot_sel, soft_sel)
    except IndexError:
        error: str = [
            "La fonction a besoin de 3 arguments",
            "SHOW SHOT SOFTWARE",
            "ex: go test tes houdini",
        ]
        create_frame(error, center=True)
        print(cmds)

import os
from rich.tree import Tree

# from rich import print


def list_shot():
    """Function for listing shots"""
    proj_dir = os.path.abspath(os.getcwd() + "/PROJECT DIRECTORY")
    my_list = os.listdir(proj_dir)
    tree = Tree("Project Directory")
    tree.guide_style = "bold"

    for i in my_list:
        if os.path.isdir(f"{proj_dir}/{i}"):
            prj_tree = tree.add(i)
            tree.guide_style = "bold"
        for s in os.listdir(f"{proj_dir}/{i}"):
            if os.path.isdir(f"{proj_dir}/{i}/{s}"):
                prj_tree.add(s)

    print(tree)

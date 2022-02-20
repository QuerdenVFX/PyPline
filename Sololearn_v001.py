import os
import json as js
import shutil
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

class Project():

    #----------------------------------------------------------------#
    #                        PROJECT Data                            #
    Name = inquirer.text(message="Project Name :").execute()
    Shot = inquirer.text(message="Shot Name :").execute()
    Resolution = inquirer.select(message= "Resolution :", choices=["1280x720", "1920x1080", "2048x1152", "3040x2160"]).execute()
    resolutionX, resolutionY = Resolution.split("x")
    resolutionX = int("".join([i for i in resolutionX if i.isdigit()]))
    resolutionY = int("".join([i for i in resolutionY if i.isdigit()]))
    
    
    FrameRate = inquirer.select(message="Frame Rate :", choices=[17, 24, 25, 30, 60, 120], default=24).execute()
    Software_choise = [Choice("Houdini", name="Houdini"),
                        Choice("Nuke", name="Nuke"),
                        Choice("Maya", name="Maya")]
    Software = inquirer.checkbox(
                            message="Select Project Software:", choices=Software_choise).execute()
    
   



    JSON_data = {"Shot" : Shot,
                "ResolutionX" : resolutionX,
                "ResolutionY" : resolutionY,
                "FrameRate" : FrameRate,
                "Software" : Software}
                        
                        

    #----------------------------------------------------------------#
    #                        PROJECT FOLDER                          #
    
    #softwareList = ["Nuke", "Houdini", "Maya"]
    BaseFolder = inquirer.text(message="Base Folder :", default=os.path.abspath(os.getcwd())).execute()
    path = os.path.abspath(f"{BaseFolder}/{Name}/{Shot}/")
    library_path = os.path.abspath(path + "/_Library")

    #----------------------------------------------------------------#

    #----------------------------------------------------------------#
    #                        SOFTWARE FOLDER  PREP.                  #

    Soft_Folder = {
                    "Houdini":["hip", "cache", "flipbook", "render", "obj"],
                    "Maya":["assets","autosave","cache","clips",'data', 'images', 'movies', 'renderData','sceneAssembly', 'scenes', 'scripts', 'sound','sourceimages','Time Editor'],
                    "Nuke":["comp","render"]
    }

    Soft_basic_file= {
                    "Houdini": os.path.abspath(f"{BaseFolder}/HOUDINI_FILE.hipnc"),
                    "Maya":"",
                    "Nuke": os.path.abspath(f"{BaseFolder}/NUKE_FILE.nk")}

    Soft_ext= {
                    "Houdini": "hipnc",
                    "Maya":"",
                    "Nuke": "nk"}

    for soft in Software:
        print(Soft_Folder[f"{soft}"])
        print(Soft_basic_file[f"{soft}"])
        
    #----------------------------------------------------------------#

    #----------------------------------------------------------------#
    #                        LIST SHOT                               #



    #----------------------------------------------------------------#

pass

print (Project.JSON_data)
def CreateMatrice():
    for i in creating_folder:
        os.mkdir(f"{Project.path}/{i}")


os.makedirs(Project.path)
os.mkdir(Project.library_path)

for soft in Project.Software:
    os.makedirs(f"{Project.path}/{soft}")
    shutil.copy(Project.Soft_basic_file[f"{soft}"], f"{Project.path}/{soft}/{Project.Shot}.{Project.Soft_ext[soft]}")

    
if Project.Software == Project.softwareList[0]:
    print(Project.Software)

    creating_folder = [Project.Software]
    for i in creating_folder:
        os.mkdir(f"{Project.path}/{i}")
    for x in Project.Nuke_folders:
        os.mkdir(f"{Project.path}/{i}/{x}")
    shutil.copy(os.path.abspath("J:/PyEnv/NUKE_FILE.nk") , os.path.abspath(f"{Project.path}/Nuke/{Project.Shot}.nk"))

elif Project.Software == Project.softwareList[1]:
    print(Project.Software, "Nuke")
    creating_folder = [Project.Software, "Nuke"]
    for i in creating_folder:
        os.mkdir(f"{Project.path}/{i}")
    for x in Project.Nuke_folders:
        os.mkdir(f"{Project.path}/{i}/{x}")
    shutil.copy(os.path.abspath("J:/PyEnv/NUKE_FILE.nk") , os.path.abspath(f"{Project.path}/Nuke/{Project.Shot}.nk"))
    shutil.copy(os.path.abspath("J:/PyEnv/HOUDINI_FILE.hipnc"), os.path.abspath(f"{Project.path}/{Project.Software}/{Project.Shot}.hipnc"))
elif Project.Software == Project.softwareList[2]:
    print(Project.Software,"Nuke")
    creating_folder = [Project.Software, "Nuke"]









configure = [Project.Name, Project.Shot, Project.Resolution, Project.FrameRate, Project.Software]
project_folder = Project.path


print (configure)
print (project_folder)

ListShot = [Project.Name]
ListInfo = js.dumps(ListShot, indent=4)
with open(os.path.abspath(f"{Project.BaseFolder}/{Project.Name}/ShotList.json"), "w") as file:
    file.write(ListInfo)


with open(os.path.abspath(f"{Project.BaseFolder}/{Project.Name}/{Project.Shot}/{Project.Shot}_data.json"), "w") as file:
    file.write(js.dumps(Project.JSON_data, indent=4))
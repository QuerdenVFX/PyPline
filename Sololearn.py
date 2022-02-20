import os
import json as js
import shutil
import inquirer

class Project():

    #----------------------------------------------------------------#
    #                        PROJECT Data                            #
    Name = input("Project Name: ")
    Shot = input("Shot: ")
    Resolution = input("Resolution: ")
    resolutionX, resolutionY = Resolution.split("x")
    resolutionX = int("".join([i for i in resolutionX if i.isdigit()]))
    resolutionY = int("".join([i for i in resolutionY if i.isdigit()]))
    
    
    FrameRate = int(input("Frame Rate: "))
    Software = input("Software: ")



    JSON_data = {"Shot" : Shot,
                "ResolutionX" : resolutionX,
                "ResolutionY" : resolutionY,
                "FrameRate" : FrameRate,
                "Software" : Software}
                        
                        

    #----------------------------------------------------------------#
    #                        PROJECT FOLDER                          #
    
    softwareList = ["Nuke", "Houdini", "Maya"]
    BaseFolder = input("Base Folder: ")
    path = os.path.abspath(f"{BaseFolder}/{Name}/{Shot}/")
    library_path = os.path.abspath(path + "/Library")

    #----------------------------------------------------------------#

    #----------------------------------------------------------------#
    #                        SOFTWARE FOLDER  TYPE                   #

    Houdini_folders = ["hip", "cache", "flipbook", "render", "obj"]
    Nuke_folders =  ["comp","render"]
    Maya_folders =["assets","autosave","cache","clips",'data', 'images', 'movies', 'renderData','sceneAssembly', 'scenes', 'scripts', 'sound','sourceimages','Time Editor'],

    #----------------------------------------------------------------#

    #----------------------------------------------------------------#
    #                        LIST SHOT                               #



    #----------------------------------------------------------------#

pass

# def CreateMatrice():
#     for i in creating_folder:
#         os.mkdir(f"{Project.path}/{i}")


os.makedirs(Project.path)
os.mkdir(Project.library_path)


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


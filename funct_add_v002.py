import os
import json as js
import shutil
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from pathlib import Path
import csv

try:
    class Project():

        dir = os.path.abspath(os.getcwd()+"/PROJECT DIRECTORY")

        my_list = os.listdir(dir)
        dictOfProjects = {i : None for i in my_list}



        #----------------------------------------------------------------#
        #                        PROJECT Data                            #
        Name = inquirer.text(message="Project Name :", completer={i : None for i in my_list}, multicolumn_complete=True).execute()
        Shot = inquirer.text(message="Shot Name :").execute()
        Resolution = inquirer.select(message= "Resolution :", choices=["1280x720", "1920x1080", "2048x1152", "3040x2160"]).execute()
        resolutionX, resolutionY = Resolution.split("x")
        resolutionX = int("".join([i for i in resolutionX if i.isdigit()]))
        resolutionY = int("".join([i for i in resolutionY if i.isdigit()]))
        
        
        FrameRate = inquirer.select(message="Frame Rate :", choices=[17, 24, 25, 30, 60, 120], default=24).execute()


        # Software_choise =  [Choice("Houdini", name="Houdini"),
        #                     Choice("Nuke", name="Nuke"),
        #                     Choice("Maya", name="Maya"),
        #                     Choice("Blender", name="Blender")]

        with open("config.csv", mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 1
            Software_choise =[]
            for row in csv_reader:
                #print(f'\t{row["software"]}, launch path is {row["path"]}, and the folder needed are {row["matrices"]}')
                Software_choise.append(Choice(row["software"], name=f'{row["software"]}')) 
                line_count+=1
            

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
        BaseFolder = inquirer.text(message="Base Folder :", default=os.path.abspath(os.getcwd()+"/PROJECT DIRECTORY")).execute()
        path = os.path.abspath(f"{BaseFolder}/{Name}/{Shot}/")
        library_path = os.path.abspath(path + "/_Library")

        #----------------------------------------------------------------#

        #----------------------------------------------------------------#
        #                        SOFTWARE FOLDER  PREP.                  #

        # Soft_Folder = {
        #                 "Houdini": ["hip","cache", "flipbook", "render", "obj"],
        #                 "Maya":["assets","autosave","cache","clips",'data', 'images', 'movies', 'renderData','sceneAssembly', 'scenes', 'scripts', 'sound','sourceimages','Time Editor'],
        #                 "Nuke":["comp","render"],
        #                 "Blender":["cache","flipbook", "render", "obj"]}
        
        with open("config.csv", mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 1
            Folders=[]
            Soft_Folder = {}
            for row in csv_reader:
                #Folders.append(row['matrices'].split(' '))
                Soft_Folder[row['software']] = row['matrices'].split(' ')
                line_count+=1
        print (Soft_Folder)
                    

        Soft_basic_file= {
                        "houdini": os.path.abspath(f"{os.getcwd()}/req/HOUDINI_FILE.hipnc"),
                        "maya":os.path.abspath(f"{os.getcwd()}/req/MAYA_FILE.mb"),
                        "nuke": os.path.abspath(f"{os.getcwd()}/req/NUKE_FILE.nk"),
                        "blender":os.path.abspath(f"{os.getcwd()}/req/BLENDER_FILE.blend")
                        }
                        

        Soft_ext=   {
                    "houdini": "hipnc",
                    "maya":"mb",
                    "nuke": "nk",
                    "blender": "blend"
                    }

        #----------------------------------------------------------------#





    #Create Directorty and first project file#
    if Path(Project.path).exists():
        pass
    else:
        os.makedirs(Project.path)
        os.mkdir(Project.library_path)

    
    for soft in Project.Software:
        for folder in Project.Soft_Folder[soft]:
            os.makedirs(os.path.abspath(f"{Project.path}/{soft}/{folder}"))
        
        
        if Path(f"{Project.path}/{soft}").exists():
            if soft == "maya":
                shutil.copy(Project.Soft_basic_file[f"{soft}"], f"{Project.path}/{soft}/scenes/{Project.Shot}_v001.{Project.Soft_ext[soft]}")
            elif soft == "nuke":
                shutil.copy(Project.Soft_basic_file[f"{soft}"], f"{Project.path}/{soft}/comp/{Project.Shot}_v001.{Project.Soft_ext[soft]}")
            elif soft == "houdini":
                shutil.copy(Project.Soft_basic_file[f"{soft}"], f"{Project.path}/{soft}/hip/{Project.Shot}_v001.{Project.Soft_ext[soft]}")
            else:
                shutil.copy(Project.Soft_basic_file[f"{soft}"], f"{Project.path}/{soft}/{Project.Shot}_v001.{Project.Soft_ext[soft]}")
            pass
        else:
            #os.makedirs(f"{Project.path}/{soft}")

            shutil.copy(Project.Soft_basic_file[f"{soft}"], f"{Project.path}/{soft}/{Project.Shot}_v001.{Project.Soft_ext[soft]}")
        

    #Create ShotList and Shot Data

    configure = [Project.Name, Project.Shot, Project.Resolution, Project.FrameRate, Project.Software]
    project_folder = Project.path



    ListShot = [Project.Shot]

    ListInfo = js.dumps(ListShot, indent=4)
    ShotList_path  =Path(os.path.abspath(f"{Project.BaseFolder}/{Project.Name}/ShotList.json"))

    # with open(ShotList_path, "w") as file:
    #     file.write(ListInfo)


    with open(os.path.abspath(f"{Project.BaseFolder}/{Project.Name}/{Project.Shot}/_Library/{Project.Shot}_data.json"), "w") as file:
        file.write(js.dumps(Project.JSON_data, indent=4))


    if ShotList_path.exists():
        with open(ShotList_path, 'r') as json_file:
            mylist = js.load(json_file)
            mylist.append(Project.Shot)

        with open(ShotList_path, 'w') as file:
            js.dump(mylist,file, indent=4)
    else:
        # json_list = js.dumps(ListShot, indent = 4)
        with open(ShotList_path, "w") as outfile:
            outfile.write(ListInfo)

except KeyboardInterrupt:
    print("CANCELED")
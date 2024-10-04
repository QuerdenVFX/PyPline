import os
import json as js
import shutil
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from pathlib import Path
import csv
from funct.frame import create_frame

def add():
    try:
        class Project():


            dir = os.path.abspath(os.getcwd()+"/PROJECT DIRECTORY")
            if not os.path.isdir(dir):
                os.mkdir(dir)

            my_list = os.listdir(dir)
            dictOfProjects = {i : None for i in my_list}

            create_frame(["Press Ctrl+C to cancel the operation to add project or shot"], center=True)

            #----------------------------------------------------------------#
            #                        PROJECT Data                            #
            
            Name = inquirer.text(message="Project Name :", completer={i : None for i in my_list}, multicolumn_complete=True).execute()
            if(os.path.exists(os.path.abspath(f"{dir}/{Name}"))):
                list_shot = os.listdir(os.path.abspath(f"{dir}/{Name}"))
                Shot = inquirer.text(message="Shot Name :", completer={i : None for i in list_shot}, multicolumn_complete=True).execute()
            else:
                Shot = inquirer.text(message="Shot Name :").execute()
            Resolution = inquirer.select(message= "Resolution :", choices=["1280x720", "1920x1080", "2048x1152", "3040x2160"]).execute()
            resolutionX, resolutionY = Resolution.split("x")
            resolutionX = int("".join([i for i in resolutionX if i.isdigit()]))
            resolutionY = int("".join([i for i in resolutionY if i.isdigit()]))
            FrameRate = inquirer.select(message="Frame Rate :", choices=[17, 24, 25, 30, 60, 120], default=24).execute()

            Software_choise = []
            with open("config.csv", mode="r") as csv_file:
                    csv_reader = csv.DictReader(csv_file)

                    for row in csv_reader:
                        software = row['software'].capitalize()
                        Software_choise.append(Choice(software, name=software))

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
            
            path = os.path.abspath(f"{dir}/{Name}/{Shot}/")
            library_path = os.path.abspath(path + "/_Library")

            #----------------------------------------------------------------#

            #----------------------------------------------------------------#
            #                        SOFTWARE FOLDER  PREP.                  #



            with open("config.csv", mode="r") as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    Soft_Folder = {}
                    Soft_ext= {}

                    for row in csv_reader:
                        software = row['software'].capitalize()
                        matrices = row['matrices'].split()
                        ext= row['extension']
                        Soft_Folder[software] = matrices
                        Soft_ext[software] = ext
                        

            Soft_basic_file= {
                            "Houdini": os.path.abspath(f"{os.getcwd()}/req//HOUDINI_FILE.hipnc"),
                            "Maya":os.path.abspath(f"{os.getcwd()}/req/MAYA_FILE.mb"),
                            "Nuke": os.path.abspath(f"{os.getcwd()}/req/NUKE_FILE.nk"),
                            "Blender":os.path.abspath(f"{os.getcwd()}/req/BLENDER_FILE.blend")
                            }
            soft_str = " - ".join(str(i) for i in Software)            
            create_frame([Name, Shot, str(FrameRate), Resolution, soft_str],center=False)
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
                
                shutil.copy(Project.Soft_basic_file[f"{soft}"], f"{Project.path}/{soft}/{Project.Shot}_v001.{Project.Soft_ext[soft]}")
                
            else:
                #os.makedirs(f"{Project.path}/{soft}")

                shutil.copy(Project.Soft_basic_file[f"{soft}"], f"{Project.path}/{soft}/{Project.Shot}_v001.{Project.Soft_ext[soft]}")
            

        #Create ShotList and Shot Data

        configure = [Project.Name, Project.Shot, Project.Resolution, Project.FrameRate, Project.Software]
        project_folder = Project.path
        


        ListShot = [Project.Shot]

        ListInfo = js.dumps(ListShot, indent=4)
        ShotList_path  =Path(os.path.abspath(f"{Project.dir}/{Project.Name}/ShotList.json"))

        # with open(ShotList_path, "w") as file:
        #     file.write(ListInfo)


        with open(os.path.abspath(f"{Project.dir}/{Project.Name}/{Project.Shot}/_Library/{Project.Shot}_data.json"), "w") as file:
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
    except FileExistsError:
        print("File already exists, creation skip")


        
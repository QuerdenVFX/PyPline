import os
import json as js
import shutil
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from os.path import exists
from pathlib import Path
from cmd import Cmd
import subprocess as sp


class MyPromt(Cmd):
    prompt= ">"
    intro="Welcome to Pypline"

    
    def do_add(self, inp):

        dir = os.path.abspath(os.getcwd()+"/PROJECT DIRECTORY")

        my_list = os.listdir(dir)
        dictOfProjects = {i : None for i in my_list}

        print(dir)

        class Project():


            


            #----------------------------------------------------------------#
            #                        PROJECT Data                            #
            Name = inquirer.text(message="Project Name :", completer={i : None for i in my_list}, multicolumn_complete=True).execute()
            Shot = inquirer.text(message="Shot Name :").execute()
            Resolution = inquirer.select(message= "Resolution :", choices=["1280x720", "1920x1080", "2048x1152", "3040x2160"]).execute()
            resolutionX, resolutionY = Resolution.split("x")
            resolutionX = int("".join([i for i in resolutionX if i.isdigit()]))
            resolutionY = int("".join([i for i in resolutionY if i.isdigit()]))
            
            
            FrameRate = inquirer.select(message="Frame Rate :", choices=[17, 24, 25, 30, 60, 120], default=24).execute()
            Software_choise =  [Choice("Houdini", name="Houdini"),
                                Choice("Nuke", name="Nuke"),
                                Choice("Maya", name="Maya"),
                                Choice("Blender", name="Blender")]
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

            Soft_Folder = {
                            "Houdini":["cache", "flipbook", "render", "obj"],
                            "Maya":["assets","autosave","cache","clips",'data', 'images', 'movies', 'renderData','sceneAssembly', 'scenes', 'scripts', 'sound','sourceimages','Time Editor'],
                            "Nuke":["comp","render"],
                            "Blender":["cache","flipbook", "render", "obj"]
                        }

            Soft_basic_file= {
                            "Houdini": os.path.abspath(f"{os.getcwd()}/HOUDINI_FILE.hipnc"),
                            "Maya":"",
                            "Nuke": os.path.abspath(f"{os.getcwd()}/NUKE_FILE.nk"),
                            "Blender":os.path.abspath(f"{os.getcwd()}/BLENDER_FILE.blend")
                            }
                            

            Soft_ext=   {
                        "Houdini": "hipnc",
                        "Maya":"",
                        "Nuke": "nk",
                        "Blender": "blend"
                        }

            #----------------------------------------------------------------#

        
        pass


        #Create Directorty and first project file#
        if Path(Project.path).exists():
            pass
        else:
            os.makedirs(Project.path)
            os.mkdir(Project.library_path)

        for soft in Project.Software:
            if Path(f"{Project.path}/{soft}").exists():
                pass
            else:
                os.makedirs(f"{Project.path}/{soft}")
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




    def do_list(self, inp):
        dir = os.path.abspath(os.getcwd()+"/PROJECT DIRECTORY")

        my_list = os.listdir(dir)

        print(my_list)

    def do_houdini(self, inp):
        os.startfile(os.path.abspath("C:/Program Files/Side Effects Software/Houdini 19.0.383/bin/houdinifx.exe"))

    def do_blender(self, inp):
        os.startfile(os.path.abspath("C:/Program Files/Blender Foundation/Blender 3.0/blender-launcher.exe"))
    
    def do_nuke(self, inp):
        os.startfile(os.path.abspath("C:/Program Files/Nuke13.0v1/Nuke13.0.exe"))

    def do_gs(self, inp):
        project = inp.split(" ")[0]
        shot = inp.split(" ")[1]
        print (project, shot)
        gs = [project, shot]
        return gs

    def do_go(self, inp):
        project = inp.split(" ")[0]
        shot = inp.split(" ")[1]
        software = inp.split(" ")[2]

        Soft_ext=   {
                        "Houdini": "hipnc",
                        "Maya":"",
                        "Nuke": "nk",
                        "Blender": "blend"
                        }
        
        for i in Soft_ext:
            if(software in i):
                
                ext = (Soft_ext[i])
        print(ext)

     

        software_path = {
                        "Houdini": os.path.abspath("C:/Program Files/Side Effects Software/Houdini 19.0.383/bin/houdinifx.exe"),
                        "Maya":"",
                        "Nuke": os.path.abspath("C:/Program Files/Nuke13.0v1/Nuke13.0.exe"),
                        "Blender": os.path.abspath("C:/Program Files/Blender Foundation/Blender 3.0/blender-launcher.exe")
                        }

        for i in software_path:
            if(software in i):
                
                soft = (software_path[i])
        print(soft)   

        houdini = os.path.abspath("C:/Program Files/Side Effects Software/Houdini 19.0.383/bin/houdinifx.exe")
        file = f"J:/PyEnv/PROJECT DIRECTORY/{project}/{shot}/{software}/{shot}_v001.{ext}"

        #print(i)

        #execute = "".join(houdini + " "+ file)
        sp.Popen([soft, file])





   
        

MyPromt().cmdloop()


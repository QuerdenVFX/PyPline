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



        #class Project():


            


        #----------------------------------------------------------------#
        #                        PROJECT Data                            #
        Project_Name = inquirer.text(message="Project Name :", completer={i : None for i in my_list}, multicolumn_complete=True).execute()
        Project_Shot = inquirer.text(message="Shot Name :").execute()
        Project_Resolution = inquirer.select(message= "Resolution :", choices=["1280x720", "1920x1080", "2048x1152", "3040x2160"]).execute()
        Project_resolutionX, Project_resolutionY = Project_Resolution.split("x")
        Project_resolutionX = int("".join([i for i in Project_resolutionX if i.isdigit()]))
        Project_resolutionY = int("".join([i for i in Project_resolutionY if i.isdigit()]))
        
        
        Project_FrameRate = inquirer.select(message="Frame Rate :", choices=[17, 24, 25, 30, 60, 120], default=24).execute()
        Project_Software_choise =  [Choice("Houdini", name="Houdini"),
                            Choice("Nuke", name="Nuke"),
                            Choice("Maya", name="Maya"),
                            Choice("Blender", name="Blender")]
        Project_Software = inquirer.checkbox(
                                message="Select Project Software:", choices=Project_Software_choise).execute()

        Project_JSON_data = {"Shot" : Project_Shot,
                    "ResolutionX" : Project_resolutionX,
                    "ResolutionY" : Project_resolutionY,
                    "FrameRate" : Project_FrameRate,
                    "Software" : Project_Software}
                            

        #----------------------------------------------------------------#
        #                        PROJECT FOLDER                          #
        
        #softwareList = ["Nuke", "Houdini", "Maya"]
        Project_BaseFolder = inquirer.text(message="Base Folder :", default=os.path.abspath(os.getcwd()+"/PROJECT DIRECTORY")).execute()
        Project_path = os.path.abspath(f"{Project_BaseFolder}/{Project_Name}/{Project_Shot}/")
        Project_library_path = os.path.abspath(Project_path + "/_Library")

        #----------------------------------------------------------------#

        #----------------------------------------------------------------#
        #                        SOFTWARE FOLDER  PREP.                  #

        Project_Soft_Folder = {
                        "Houdini":["cache", "flipbook", "render", "obj"],
                        "Maya":["assets","autosave","cache","clips",'data', 'images', 'movies', 'renderData','sceneAssembly', 'scenes', 'scripts', 'sound','sourceimages','Time Editor'],
                        "Nuke":["comp","render"],
                        "Blender":["cache","flipbook", "render", "obj"]
                    }

        Project_Soft_basic_file= {
                        "Houdini": os.path.abspath(f"{os.getcwd()}/HOUDINI_FILE.hipnc"),
                        "Maya":"",
                        "Nuke": os.path.abspath(f"{os.getcwd()}/NUKE_FILE.nk"),
                        "Blender":os.path.abspath(f"{os.getcwd()}/BLENDER_FILE.blend")
                        }
                        

        Project_Soft_ext=   {
                    "Houdini": "hipnc",
                    "Maya":"",
                    "Nuke": "nk",
                    "Blender": "blend"
                    }

        #----------------------------------------------------------------#

        
        


        #Create Directorty and first project file#
        if Path(Project_path).exists():
            pass
        else:
            os.makedirs(Project_path)
            os.mkdir(Project_library_path)

        for soft in Project_Software:
            if Path(f"{Project_path}/{soft}").exists():
                pass
            else:
                os.makedirs(f"{Project_path}/{soft}")
                shutil.copy(Project_Soft_basic_file[f"{soft}"], f"{Project_path}/{soft}/{Project_Shot}_v001.{Project_Soft_ext[soft]}")

        #Create ShotList and Shot Data

        configure = [Project_Name, Project_Shot, Project_Resolution, Project_FrameRate, Project_Software]
        project_folder = Project_path



        ListShot = [Project_Shot]

        ListInfo = js.dumps(ListShot, indent=4)
        ShotList_path  =Path(os.path.abspath(f"{Project_BaseFolder}/{Project_Name}/ShotList.json"))

        # with open(ShotList_path, "w") as file:
        #     file.write(ListInfo)


        with open(os.path.abspath(f"{Project_BaseFolder}/{Project_Name}/{Project_Shot}/_Library/{Project_Shot}_data.json"), "w") as file:
            file.write(js.dumps(Project_JSON_data, indent=4))


        if ShotList_path.exists():
            with open(ShotList_path, 'r') as json_file:
                mylist = js.load(json_file)
                mylist.append(Project_Shot)

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





   
        
if __name__ == "__main__":
    MyPromt().cmdloop()


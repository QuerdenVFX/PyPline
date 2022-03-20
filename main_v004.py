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
    def do_send(self, line):
        pass
      
    
    def do_exit(self, inp):
        return True


    def do_add(self, inp):

        os.system("funct_add.py")

        pass

    def do_conf(self,inp):
        os.system("config_path.py")


    def do_list(self, inp):
        dir = os.path.abspath(os.getcwd()+"/PROJECT DIRECTORY")
        
        my_list = os.listdir(dir)
        for i in my_list:
            print (i)


        #print(my_list)

    def do_houdini(self, inp):
        os.startfile(os.path.abspath("C:/Program Files/Side Effects Software/Houdini 19.0.383/bin/houdinifx.exe"))

    def do_blender(self, inp):
        os.startfile(os.path.abspath("C:/Program Files/Blender Foundation/Blender 3.0/blender-launcher.exe"))
    
    def do_nuke(self, inp):
        os.startfile(os.path.abspath("C:/Program Files/Nuke13.0v1/Nuke13.0.exe"))

    # def do_gs(self, inp):
    #     project = inp.split(" ")[0]
    #     shot = inp.split(" ")[1]
    #     print (project, shot)
    #     gs = [project, shot]
    #     return gs

    def do_go(self, inp):
        project = inp.split(" ")[0]
        shot = inp.split(" ")[1]
        software = inp.split(" ")[2]

        Soft_ext=   {
                        "houdini": "hipnc",
                        "maya":"",
                        "nuke": "nk",
                        "blender": "blend"
                        }
        
        for i in Soft_ext:
            if(software in i):
                
                ext = (Soft_ext[i])
        

     

        software_path = {
                        "houdini": os.path.abspath("C:/Program Files/Side Effects Software/Houdini 19.0.383/bin/houdinifx.exe"),
                        "maya":"",
                        "nuke": os.path.abspath("C:/Program Files/Nuke13.0v1/Nuke13.0.exe"),
                        "blender": os.path.abspath("C:/Program Files/Blender Foundation/Blender 3.0/blender-launcher.exe")
                        }

        for i in software_path:
            if(software in i):
                
                soft = (software_path[i])
           

        houdini = os.path.abspath("C:/Program Files/Side Effects Software/Houdini 19.0.383/bin/houdinifx.exe")

        if(soft == "houdini"):
            file = f"J:/PyEnv/PROJECT DIRECTORY/{project}/{shot}/Houdini/hip/{shot}_v001.{ext}"
               
        elif(soft == "maya"):
            file = f"J:/PyEnv/PROJECT DIRECTORY/{project}/{shot}/Maya/scenes/{shot}_v001.{ext}"
               
        elif(soft == "nuke"):
            file = f"J:/PyEnv/PROJECT DIRECTORY/{project}/{shot}/Nuke/comp/{shot}_v001.{ext}"
                          
        else:
             file = f"J:/PyEnv/PROJECT DIRECTORY/{project}/{shot}/Blender/{shot}_v001.{ext}"
            


        #print(i)

        #execute = "".join(houdini + " "+ file)
        sp.Popen([soft, os.path.abspath(file)])





   
        
if __name__ == '__main__':

    MyPromt().cmdloop()
    

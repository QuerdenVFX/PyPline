import os
import json as js
import shutil
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from os.path import exists
from pathlib import Path
from cmd import Cmd
import subprocess as sp
import csv



try:
    class MyPromt(Cmd):
        prompt= ">"

        intro="Welcome to Pypline"
        def do_send(self, line):
            pass
        
        
        def do_exit(self, inp):
            return True


        def do_add(self, inp):

            os.system("funct_add_v002.py")

            pass

        def do_conf(self,inp):
            os.system("config_path.py")


        def do_list(self, inp):
            dir = os.path.abspath(os.getcwd()+"/PROJECT DIRECTORY")
            
            my_list = os.listdir(dir)
            for i in my_list:
                print (i)


            #print(my_list)
        with open("config.csv", mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 1

            for row in csv_reader:
                funct = f"do_{row['software']}"
                exec(f"def do_{row['software']}(self, inp):\n\tos.startfile(os.path.abspath(f\'{row['path']}\'))")
                line_count+=1
                
        # def do_houdini(self, inp):
        #     os.startfile(os.path.abspath("C:/Program Files/Side Effects Software/Houdini 19.0.561/bin/houdinifx.exe"))

        # def do_blender(self, inp):
        #     os.startfile(os.path.abspath("C:/Program Files/Blender Foundation/Blender 3.0/blender-launcher.exe"))
        
        # def do_nuke(self, inp):
        #     os.startfile(os.path.abspath("C:/Program Files/Nuke13.0v1/Nuke13.0.exe"))

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
            

        

            # software_path = {
            #                 "houdini": os.path.abspath("C:/Program Files/Side Effects Software/Houdini 19.0.561/bin/houdinifx.exe"),
            #                 "maya":"",
            #                 "nuke": os.path.abspath("C:/Program Files/Nuke13.0v1/Nuke13.0.exe"),
            #                 "blender": os.path.abspath("C:/Program Files/Blender Foundation/Blender 3.0/blender-launcher.exe")
            #                 }
            with open("config.csv", mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                line_count = 1
                software_path = {}
                for row in csv_reader:
                    #Folders.append(row['matrices'].split(' '))
                    software_path[row['software']] = row['path']
                    line_count+=1


            for i in software_path:
                if(software in i):
                    
                    soft = (software_path[i])
            

            #houdini = os.path.abspath("C:/Program Files/Side Effects Software/Houdini 19.0.383/bin/houdinifx.exe")

            if(software == "houdini"):
                file = os.path.abspath(f"./PROJECT DIRECTORY/{project}/{shot}/Houdini/hip/{shot}_v001.{ext}")
                
            elif(software == "maya"):
                file = os.path.abspath(f"./PROJECT DIRECTORY/{project}/{shot}/Maya/scenes/{shot}_v001.{ext}")
                
            elif(software == "nuke"):
                file = os.path.abspath(f"./PROJECT DIRECTORY/{project}/{shot}/Nuke/comp/{shot}_v001.{ext}")
                            
            else:
                file = os.path.abspath(f"./PROJECT DIRECTORY/{project}/{shot}/Blender/{shot}_v001.{ext}")
                


            #print(i)

            #execute = "".join(houdini + " "+ file)
            sp.Popen([soft, os.path.abspath(file)])




    
            
    if __name__ == '__main__':

        MyPromt().cmdloop()

except KeyboardInterrupt:
    print("Close PyPline")
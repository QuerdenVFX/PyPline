import os
from cmd import Cmd
import csv
import xml.etree.ElementTree as ET
import functions.open as fOpen
import functions.add as fAdd
import functions.config as fConf


commands = {
        "add": "Créer un nouveau projet ou shot",
        "conf": "Coonfiguration de la liste des logiciels",
        "list": "Liste les differents projets",
        "go": "Lance un logiciel avec le projet et la shot selectionné", 
    }

class MyPromt(Cmd):

    prompt = ">"

    intro = "Welcome to Pypline"
    
    # def do_test(self,inp):
    #     print(test0123.test())

    def do_help(self, inp):
        print("#============================================================================#")
        for command, description in commands.items():
            print(f"   {command}: {description}    ")
        print("#============================================================================#")

    def do_exit(self, inp):
        return True

    def do_add(self, inp):
        fAdd.add()
        create_dynamic_commands()

    def do_conf(self, inp):
        fConf.conf()

    def do_list(self, inp):
        dir = os.path.abspath(os.getcwd() + "/PROJECT DIRECTORY")
        my_list = os.listdir(dir)
        print("#========== Project List ==========#")
        for i in my_list:
            print(i)
        print("#==================================#")

    def do_go(self, inp):
        fOpen.openShot(inp)


    
# Fonction pour ajouter dynamiquement les commandes basées sur config.csv
def create_dynamic_commands():
    with open("config.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            software = row['software']
            path = row['path']
            commands[software] = f"Execute le programme {software}"

            # Crée une méthode qui ouvre le logiciel à partir du chemin dans config.csv
            def dynamic_method(self, inp, path=path):
                os.startfile(path)

            # Utilise setattr pour ajouter cette méthode à MyPromt
            setattr(MyPromt, f'do_{software}', dynamic_method)

if __name__ == '__main__':
    create_dynamic_commands()
    MyPromt().cmdloop()


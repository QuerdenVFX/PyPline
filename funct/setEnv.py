import xml.etree.ElementTree as ET
from funct.frame import create_frame
def set(shot):
    xml_path = 'C:/Users/Gautier/Documents/houdini20.5/MainMenuCommon.xml'

    # Charger le fichier XML
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Trouver l'élément <menuBar>
    menu_bar = root.find(".//menuBar")

    if menu_bar is not None:
        # Créer l'élément <subMenu>
        submenu = ET.Element("subMenu", {"id": "shot"})

        # Ajouter l'élément <label> avec son attribut
        label = ET.SubElement(submenu, "label", {"id": "shot_name"})
        label.text = f"SHOT --> [{shot}]"

        # Ajouter un élément <separatorItem>
        separator1 = ET.SubElement(submenu, "separatorItem")

        # Ajouter <scriptItem> avec un enfant <label> et <scriptCode>
        script_item = ET.SubElement(submenu, "scriptItem", {"id": "init"})
        
        # Sous-élément <label> dans <scriptItem>
        script_label = ET.SubElement(script_item, "label")
        script_label.text = "Initialize"
        
        # Sous-élément <scriptCode> dans <scriptItem>
        script_code = ET.SubElement(script_item, "scriptCode")
        script_code.text = '''import pipeline.initialize as ini
ini.initialize()'''

        # Ajouter un deuxième <separatorItem>
        separator2 = ET.SubElement(submenu, "separatorItem")

         # Trouver le dernier sous-menu dans <menuBar>
        last_submenu_index = -1
        for i, elem in enumerate(menu_bar):
            if elem.tag == "subMenu":
                last_submenu_index = i

        # Si un sous-menu a été trouvé, on insère après le dernier, sinon on l'ajoute à la fin
        if last_submenu_index != -1:
            menu_bar.insert(last_submenu_index + 1, submenu)
        else:
            menu_bar.append(submenu)

        # Sauvegarder le fichier modifié
        tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    else:
        print("<menuBar> not found in the XML.")

def remove():
    xml_path = 'C:/Users/Gautier/Documents/houdini20.5/MainMenuCommon.xml'
   
    # Charger le fichier XML
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Trouver l'élément <menuBar>
    menu_bar = root.find(".//menuBar")
    

    if menu_bar is not None:
        submenu_bar = root.find(".//subMenu[@id='shot']")
        if submenu_bar is not None:
            menu_bar.remove(submenu_bar)
            create_frame(["Environment reset"], center=True)
            
        
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)


    

    
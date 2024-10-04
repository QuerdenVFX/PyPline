import tkinter as tk

from tkinter import filedialog, messagebox, ttk
import os
import csv
from csv import writer
import pandas as pd


def conf():
    # initalise the tkinter GUI
    root = tk.Tk()

    root.title("Configuration Softwares")
    root.geometry("850x450")  # set the root dimensions
    root.pack_propagate(
        False
    )  # tells the root to not let the widgets inside it determine its size.
    root.resizable(0, 0)  # makes the root window fixed in size.

    # Frame for TreeView
    frame1 = tk.LabelFrame(root, text="Soft Data")
    frame1.place(height=200, width=800, relx=0.025)

    # Frame for edit file
    edit_frame = tk.LabelFrame(root, text="Edit")
    edit_frame.place(height=200, width=800, rely=0.45, relx=0.025)

    soft_lb = tk.Label(edit_frame, text="Software:")
    soft_lb.place(relx=0, rely=0)

    soft_en = tk.Entry(edit_frame)
    soft_en.place(relx=0.2, rely=0, height=20, width=300)

    path_lb = tk.Label(edit_frame, text="Path:")
    path_lb.place(relx=0, rely=0.2)

    path_en = tk.Entry(edit_frame)
    path_en.place(relx=0.2, rely=0.2, height=20, width=300)

    folders_lb = tk.Label(edit_frame, text="Folders:")
    folders_lb.place(relx=0, rely=0.4)

    folders_en = tk.Entry(edit_frame)
    folders_en.place(relx=0.2, rely=0.4, height=20, width=300)

    ext_lb = tk.Label(edit_frame, text="Extensions:")
    ext_lb.place(relx=0, rely=0.6)

    ext_en = tk.Entry(edit_frame)
    ext_en.place(relx=0.2, rely=0.6, height=20, width=300)

    # Buttons
    button2 = tk.Button(edit_frame, text="Reload", command=lambda: reload())
    button2.place(rely=0.8, relx=0.30)

    add_bt = tk.Button(edit_frame, text="+", height=1, width=2, command=lambda: add())
    add_bt.place(rely=0.8, relx=0.1)

    remove_bt = tk.Button(
        edit_frame, text="-", height=1, width=2, command=lambda: remove()
    )
    remove_bt.place(rely=0.8, relx=0.15)

    update_bt = tk.Button(edit_frame, text="Update", command=lambda: update())
    update_bt.place(rely=0.8, relx=0.5)

    def on_tree_select(event):
        """Function to load the selected row into the entry boxes"""
        try:
            global selected_row
            selected = tv1.selection()[0]
            selected_row = tv1.item(selected, "values")
            soft_en.delete(0, tk.END)
            soft_en.insert(0, selected_row[0])
            path_en.delete(0, tk.END)
            path_en.insert(0, selected_row[1])
            folders_en.delete(0, tk.END)
            folders_en.insert(0, selected_row[2])
            ext_en.delete(0, tk.END)
            ext_en.insert(0, selected_row[3])
        except IndexError:
            return None

    # Treeview Widget
    tv1 = ttk.Treeview(frame1)
    tv1.place(
        relheight=1, relwidth=1
    )  # set the height and width of the widget to 100% of its container (frame1).

    treescrolly = tk.Scrollbar(
        frame1, orient="vertical", command=tv1.yview
    )  # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(
        frame1, orient="horizontal", command=tv1.xview
    )  # command means update the xaxis view of the widget
    tv1.configure(
        xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set
    )  # assign the scrollbars to the Treeview Widget
    treescrollx.pack(
        side="bottom", fill="x"
    )  # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(
        side="right", fill="y"
    )  # make the scrollbar fill the y axis of the Treeview widget

    tv1.bind("<<TreeviewSelect>>", on_tree_select)  # Bind the select event

    # Global variable to store the selected row
    selected_row = None

    def add():
        if path_en.get() == "":
            add_info = [
                soft_en.get(),
                "#    Path not Defined    #",
                folders_en.get(),
                ext_en.get(),
            ]
        else:
            add_info = [
                soft_en.get(),
                os.path.abspath(path_en.get()),
                folders_en.get(),
                ext_en.get(),
            ]
        with open("config.csv", "a", newline="") as csv_file:
            csv_writer = writer(csv_file)
            csv_writer.writerow(add_info)

        reload()
        update_csv()

    def remove():
        selected = tv1.selection()[0]
        tv1.delete(selected)
        selected = ""
        update_csv()

    def reload():
        """If the file selected is valid this will load the file into the Treeview"""
        file_path = os.path.abspath("./config.csv")
        try:
            df = pd.read_csv(file_path)
        except ValueError:
            tk.messagebox.showerror(
                "Information", "The file you have chosen is invalid"
            )
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        soft_en.delete(0, tk.END)
        path_en.delete(0, tk.END)
        folders_en.delete(0, tk.END)
        ext_en.delete(0, tk.END)

        clear_data()
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)  # let the column heading = column name

        df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            tv1.insert("", "end", values=row)  # inserts each list into the treeview
        return None

    def clear_data():
        tv1.delete(*tv1.get_children())
        return None

    def update():
        """Update the selected row with new values and rewrite the CSV file"""
        # Vérifier si une ligne est sélectionnée
        selected_items = tv1.selection()
        if not selected_items:
            tk.messagebox.showwarning(
                "Avertissement", "Veuillez sélectionner une ligne à mettre à jour."
            )
            return

        selected_item = selected_items[0]  # Récupère l'élément sélectionné
        if path_en.get() == "":
            new_values = [
                soft_en.get(),
                "#    Path not Defined    #",
                folders_en.get(),
                ext_en.get(),
            ]
        else:
            new_values = [
                soft_en.get(),
                path_en.get(),
                folders_en.get(),
                ext_en.get(),
            ]  # Récupère les nouvelles valeurs des champs d'entrée

        # Mise à jour de l'affichage dans le Treeview
        tv1.item(selected_item, values=new_values)
        update_csv()
        reload()

    def update_csv():
        # Récupérer toutes les données du Treeview
        tree_data = []
        for row_id in tv1.get_children():
            row_values = tv1.item(row_id, "values")
            tree_data.append(row_values)

        # Écrire ces données dans le fichier CSV
        with open("config.csv", "w", newline="") as file:
            writer = csv.writer(file)

            # Écrire l'en-tête (colonnes)
            writer.writerow(tv1["columns"])

            # Écrire les lignes
            writer.writerows(tree_data)

    reload()
    root.mainloop()

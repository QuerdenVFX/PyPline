import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import csv
from csv import writer
import pandas as pd

# initalise the tkinter GUI
root = tk.Tk()

root.geometry("800x400") # set the root dimensions
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
root.resizable(0, 0) # makes the root window fixed in size.

# Frame for TreeView
frame1 = tk.LabelFrame(root, text="Soft Data")
frame1.place(height=200, width=800)


# Frame for edit file
edit_frame = tk.LabelFrame(root, text="Edit")
edit_frame.place(height=150, width=800, rely=0.5, relx=0)

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


# Buttons
# button1 = tk.Button(edit_frame, text="Browse A File", command=lambda: File_dialog())
# button1.place(rely=0.65, relx=0.50)

button2 = tk.Button(edit_frame, text="Reload", command=lambda: reload())
button2.place(rely=0.65, relx=0.30)

add_bt = tk.Button(edit_frame, text="Add", command=lambda: add())
add_bt.place(rely=0.65, relx=0.1)

save_bt = tk.Button(edit_frame, text="Save", command=lambda: ''())
save_bt.place(rely=0.65, relx=0.15)



## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget



def add():
    info = f"Soft:{soft_en.get()}\nPath:{path_en.get()}\nFolders: {folders_en.get()}"
    add_info = [soft_en.get(),os.path.abspath(path_en.get()), folders_en.get()]
    print(add_info)

    with open ("config.csv","a", newline="") as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(add_info)
    
with open("config.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count==0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["software"]}, launch path is {row["path"]}, and the folder needed are {row["matrices"]}')
        line_count+=1
    print(f'Process {line_count} lines.')

def reload():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = os.path.abspath("I:\PyPline\config.csv")
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    return None


root.mainloop()
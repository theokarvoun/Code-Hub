import subprocess
from tkinter import filedialog
import customtkinter as ctk
import tkinter as tk
import webbrowser as web
import os
from PIL import Image

def new(project_menu) -> None:
    def browse_directory() -> str:
        directory_path = filedialog.askdirectory()
        return directory_path

    def make_project(name, lang):
        command = f"ch -init {name} {lang}"
        if os.system(command) == 0:
            cfg_manager(mode="append", data=name)
            update_project_menu(project_menu)

    win = ctk.CTk()
    win.geometry("500x200")
    win.title("New Project")
    
    label1 = ctk.CTkLabel(win, text="Select Directory", font=("Colibri", 15))
    label1.pack(side="left", padx=10, pady=10)
    
    dir_button = ctk.CTkButton(win, text="Browse", command=lambda: label1.configure(text=browse_directory()))
    dir_button.pack(side="right", padx=10, pady=10)
    
    name_entry = ctk.CTkEntry(win, font=("Colibri", 15))
    name_entry.insert(0, "Enter Project Name")
    name_entry.pack(side="top", padx=10, pady=10)
    
    languages = ["Python", "C", "C++", "Java", "JavaScript"]
    max_length = max(len(lang) for lang in languages)
    combo_width = max_length * 12

    lang_menu = ctk.CTkComboBox(win, values=languages, width=combo_width)
    lang_menu.pack(side="bottom", padx=10, pady=10)
    
    create_button = ctk.CTkButton(win, text="Create", command=lambda: (make_project(name=os.path.join(label1.cget("text"), name_entry.get()), lang=lang_menu.get()), win.destroy()))
    create_button.pack(side="bottom", padx=10, pady=10)
    
    win.mainloop()

def cfg_manager(mode, data=None):
    if mode == "read":
        with open("config.cfg", "r") as cfg:
            return cfg.read().splitlines()
    elif mode == "append":
        with open("config.cfg", "a") as cfg:
            cfg.write(data + "\n")
    elif mode == "remove":
        with open("config.cfg", "r+") as cfg:
            lines = cfg.readlines()
            cfg.seek(0)
            for line in lines:
                if line.strip() != data:
                    cfg.write(line)
            cfg.truncate()

def add(project_menu):
    dir = browse_directory()
    if dir:
        cfg_manager(mode="append", data=dir)
        update_project_menu(project_menu)

def browse_directory() -> str:
    root = tk.Tk()
    root.withdraw()
    directory_path = filedialog.askdirectory()
    root.destroy()
    return directory_path

def make_project(name, lang):
    command = f"ch -init {name} {lang}"
    if os.system(command) == 0:
        cfg_manager(mode="append", data=name)

def version() -> str:
    try:
        proc = subprocess.Popen("ch -version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if stdout:
            #versionPresenter(stdout.decode() + "\nGUI Version alpha-v0.1.0")
            return stdout.decode()
        else:
            print("No output received.")
            return None
    except Exception as e:
        print("Error:", e)
        return None

def versionPresenter(buffer) -> None:
    tempwindow = ctk.CTk()
    tempwindow.geometry('775x200')
    tempwindow.title("Version")
    label = ctk.CTkLabel(tempwindow, text=buffer, font=("Colibri", 15))
    label.pack(padx=10, pady=10)
    button = ctk.CTkButton(tempwindow, text="Go To GitHub", command=lambda: (web.open_new_tab("https://github.com/theokarvoun/Code-Hub"), tempwindow.destroy()))
    button.pack(padx=10, pady=10)
    tempwindow.mainloop()

def update_project_menu(project_menu):
    project_names = cfg_manager(mode="read")
    if project_names:
        project_menu.configure(values=project_names)
        project_menu.set(project_names[0])
    else:
        project_menu.configure(values=["No Projects Available"])
        project_menu.set("No Projects Available")

def settings():

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    settingswindow = ctk.CTk()
    version_panel = ctk.CTkFrame(settingswindow,fg_color=settingswindow._fg_color)
    version_label_CLI = ctk.CTkLabel(version_panel,text=version())
    version_label_CLI.pack(padx=10,pady=10)
    version_label_GUI = ctk.CTkLabel(version_panel,text="GUI Version alpha-v0.1.0")
    version_label_GUI.pack(padx=10,pady=10)
    GitHubButton = ctk.CTkButton(version_panel, text="Go To GitHub", command=lambda: (web.open_new_tab("https://github.com/theokarvoun/Code-Hub")))
    GitHubButton.pack(padx=10, pady=10)
    settingswindow.geometry("500x500")
    settingswindow.title("Settings")
    menu = ctk.CTkFrame(settingswindow)
    menu.pack(side="left", fill="y")
    version_button = ctk.CTkButton(menu, text="Version",fg_color=menu._fg_color,corner_radius=0, command=lambda:(version_panel.pack(fill="both",expand=True),version_button.configure(fg_color=version_button._hover_color)))
    
    version_button.pack(side="bottom", padx=0, pady=0)

    settingswindow.mainloop()

def main() -> None:
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    window = ctk.CTk()
    window.geometry("500x500")
    window.title("Code Hub")

    menubar_frame = ctk.CTkFrame(window)
    menubar_frame.pack(side="left", fill="y")
    
    project_menu = ctk.CTkComboBox(window, width=1000)
    project_menu.set("Select Project")
    project_menu.pack(pady=10)

    # Load gear icon image
    gear_icon = Image.open("gear.png")
    gear_icon = ctk.CTkImage(gear_icon, size=(20, 20))

    settings_button = ctk.CTkButton(menubar_frame, image=gear_icon,text="", command=settings)
    settings_button.pack(side="bottom", padx=10, pady=5)
    new_button = ctk.CTkButton(menubar_frame, text="New", command=lambda: new(project_menu))
    new_button.pack(side="top", padx=10, pady=5)
    add_button = ctk.CTkButton(menubar_frame, text="Add", command=lambda: add(project_menu))
    add_button.pack(side="top", padx=10, pady=5)

    update_project_menu(project_menu)

    vscode_button = ctk.CTkButton(window, text="Open In VSCode", width=800, command=lambda: os.system(f"code {project_menu.get()}"))
    vscode_button.pack(padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()

import subprocess
from tkinter import filedialog, ttk
import customtkinter as ctk
import tkinter as tk
import webbrowser as web

def new() -> None:
    win = ctk.CTk()
    win.geometry("500x300")
    win.title("New Project")
    label1 = ctk.CTkLabel(win, text="Select Directory", font=("Colibri", 15))
    label1.pack(side="left")
    dir_button = ctk.CTkButton(win, text="Browse", command=lambda: label1.configure(text=browse_directory()))
    dir_button.pack(side="right")
    name_entry = ctk.CTkEntry(win, font=("Colibri", 15))
    name_entry.insert(0, "Enter Project Name")  # Insert default text
    name_entry.pack(side="bottom", padx=10, pady=10)

    # Create custom dropdown menu for language selection
    languages = ["Python", "C", "C++", "Java", "JavaScript"]  # List of languages
    selected_language = tk.StringVar()  # Variable to store selected language
    selected_language.set(languages[0])  # Set default value

    # Calculate the width of the longest item
    max_length = max(len(lang) for lang in languages)
    # Set the width of the dropdown menu based on the length of the longest item
    menu_width = max_length * 8  # Adjust this multiplier as needed
    
    # Style the dropdown menu
    optionmenu_style = ttk.Style()
    optionmenu_style.theme_use("clam")  # Use a different theme to match the rest of the app
    optionmenu_style.configure("TMenubutton", font=("Colibri", 12), padding=5)

    language_menu = tk.OptionMenu(win, selected_language, *languages)
    language_menu.config(width=menu_width)  # Set the width of the menu
    language_menu.pack(side="bottom", padx=10, pady=10)

    win.mainloop()

def browse_directory() -> str:
    """Open a file dialog to browse the file system and select a directory."""
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    
    directory_path = filedialog.askdirectory()
    return directory_path

def version() -> None:
    try:
        proc = subprocess.Popen("ch -version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if stdout:
            versionPresenter(stdout.decode())  # Decode bytes to string
        else:
            print("No output received.")
    except Exception as e:
        print("Error:", e)

def versionPresenter(buffer) -> None:
    tempwindow = ctk.CTk()
    tempwindow.geometry('775x200')
    tempwindow.title("CLI Version")
    label = ctk.CTkLabel(tempwindow, text=buffer, font=("Colibri", 15))
    label.pack(padx=10, pady=10)
    button = ctk.CTkButton(tempwindow,text="Go To GitHub",command=lambda: (web.open_new_tab("https://github.com/theokarvoun/Code-Hub") , tempwindow.destroy()))
    button.pack(padx=10,pady=10)
    tempwindow.mainloop()

def main() -> None:
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    # Create a root window with CustomTkinter
    window = ctk.CTk()
    window.geometry("500x500")
    window.title("Code Hub")

    # Create a custom frame for the menu bar
    menubar_frame = ctk.CTkFrame(window)

    # Create custom menu items using standard tkinter widgets
    version_button = ctk.CTkButton(menubar_frame, text="Version", command=version)
    version_button.pack(side="bottom", padx=10, pady=5)
    new_button = ctk.CTkButton(menubar_frame,text="New",command=new)
    new_button.pack(side="top",padx=10,pady=5)

    # Pack the menu bar frame to the left side
    menubar_frame.pack(side="left", fill="y")

    window.mainloop()



if __name__ == "__main__":
    main()
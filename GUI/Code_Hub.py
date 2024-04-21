import subprocess
import customtkinter as ctk
import tkinter as tk
import webbrowser as web
import platform

def version() -> None:
    try:
        proc = subprocess.Popen("ch.exe -version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
    version_button._apply_geometry_scaling
    version_button._bg_color = "black"
    version_button.pack(side="left", padx=10, pady=5)

    # Pack the menu bar frame
    menubar_frame.pack(fill="x")

    window.mainloop()



if __name__ == "__main__":
    main()
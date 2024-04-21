import subprocess
import customtkinter as ctk

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
    tempwindow.mainloop()


def main() -> None:
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    window = ctk.CTk()
    window.geometry("500x500")
    window.title("Code Hub");
    button = ctk.CTkButton(window,text="Test",command=version)
    button.pack(padx=10,pady=10)
    window.mainloop()

if __name__ == "__main__":
    main()
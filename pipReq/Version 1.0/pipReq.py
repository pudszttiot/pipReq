import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Module GUI")
        self.iconbitmap("G:\Software\py\Python Creations\Completed\Projects\pipReq\Images\pip.ico")  # Replace with the path to your icon file

        self.create_buttons()

    def create_buttons(self):
        pipreqs_button = tk.Button(self, text="Run pipreqs", command=self.run_pipreqs)
        pipreqs_button.pack(pady=10)

        pip_check_button = tk.Button(self, text="Run pip check", command=self.run_pip_check)
        pip_check_button.pack(pady=10)

        pur_button = tk.Button(self, text="Run pur", command=self.run_pur)
        pur_button.pack(pady=10)

        freeze_button = tk.Button(self, text="Run pip freeze", command=self.run_freeze)
        freeze_button.pack(pady=10)

    def run_command(self, command):
        try:
            output = subprocess.check_output(
                command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True
            )
            print(output)
            self.show_output_dialog("Command Result", output)
        except subprocess.CalledProcessError as e:
            print(e.output)
            self.show_output_dialog("Command Error", e.output)

    def show_output_dialog(self, title, message):
        messagebox.showinfo(title, message)

    def run_pipreqs(self):
        self.run_command("pipreqs .")

    def run_pip_check(self):
        self.run_command("python -m pip check")

    def run_pur(self):
        self.run_command("pur -r requirements.txt")

    def run_freeze(self):
        self.run_command("pip freeze > requirements.txt")

if __name__ == "__main__":
    app = Application()
    app.iconbitmap("G:\Software\py\Python Creations\Completed\Projects\pipReq\Images\pip.ico")  # Set your custom icon file path here
    app.mainloop()

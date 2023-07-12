import subprocess
from tkinter import messagebox, simpledialog
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
import tkinter as tk


class Application(ThemedTk):
    def __init__(self):
        super().__init__(theme="clam")
        self.title("Python Module GUI")
        self.iconbitmap(r"..\Images\pip.ico")

        self.background_image = ImageTk.PhotoImage(Image.open(r"..\Images\pipreqbg6.png"))
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_buttons()
        self.add_watermark_label()

    def create_buttons(self):
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12))

        pipreqs_button = ttk.Button(self, text="Run pipreqs", command=self.run_pipreqs)
        pipreqs_button.pack(pady=5)
        self.add_tooltip(pipreqs_button, "△ Automatically detects required tools and modules\n△ This is needed for your Python program to work correctly\n△ Generates a 'requirements.txt' file")

    def add_watermark_label(self):
        watermark_text = "pudszTTIOT"

        # Create the watermark label with the specified text
        watermark_label = tk.Label(self, text=watermark_text, font=("Corbel", 9), fg="#9aa44d", bg="#1F1D1B")
        watermark_label.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-10)

        # Custom Separator
        self.add_separator()

        pip_check_button = ttk.Button(self, text="Run pip check", command=self.run_pip_check)
        pip_check_button.pack(pady=5)
        self.add_tooltip(pip_check_button, "△ Check installed packages for issues")

        # Custom Separator
        self.add_separator()

        pur_button = ttk.Button(self, text="Run pur", command=self.run_pur)
        pur_button.pack(pady=5)
        self.add_tooltip(pur_button, "△ Updates your packages to the latest versions\n△ It only modifies your 'requirements.txt' file\n△ Never modifies your environment or installed packages")

        # Custom Separator
        self.add_separator()

        freeze_button = ttk.Button(self, text="Run pip freeze", command=self.run_freeze)
        freeze_button.pack(pady=5)
        self.add_tooltip(freeze_button, "△ Outputs a list of all installed Python modules with their versions\n△ Generates a 'requirements.txt' file")

        # Custom Separator
        self.add_separator()

        install_button = ttk.Button(self, text="Install requirements.txt", command=self.run_install_requirements)
        install_button.pack(pady=5)
        self.add_tooltip(install_button, "△ Installs all of the modules listed in the 'requirements.txt' file")

    def add_tooltip(self, widget, text):
        widget.bind("<Enter>", lambda event: self.show_tooltip(event, text))
        widget.bind("<Leave>", lambda event: self.hide_tooltip())

    def show_tooltip(self, event, text):
        x = self.winfo_rootx() + event.widget.winfo_x() + event.widget.winfo_width() + 10
        y = self.winfo_rooty() + event.widget.winfo_y() + event.widget.winfo_height() + 10

        self.tooltip = tk.Toplevel(self)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=text, bg="#FFFFD1", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self):
        if hasattr(self, 'tooltip'):
            self.tooltip.destroy()

    def add_separator(self):
        style = ttk.Style()
        style.configure("CustomSeparator.TSeparator", background="#FF0EF3")
        separator = ttk.Separator(self, orient=tk.HORIZONTAL, style="CustomSeparator.TSeparator")
        separator.pack(fill=tk.X, pady=5)

    def run_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            self.show_output_dialog("Command Result", output)
        except subprocess.CalledProcessError as e:
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

    def run_install_requirements(self):
        self.run_command("pip install -r requirements.txt")


if __name__ == "__main__":
    app = Application()
    app.iconbitmap(r"..\Images\pip.ico")
    app.mainloop()

import tkinter as tk
from tkinter import messagebox  # Importing messagebox explicitly

class ServerWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login Panel")

        # Header
        self.header_label = tk.Label(master, text="LOGIN", font=("Helvetica", 16, "bold"))
        self.header_label.pack(pady=10)

        # Entry for Name
        self.name_entry_label = tk.Label(master, text="Enter Name:")
        self.name_entry_label.pack(pady=5)
        self.name_entry_var = tk.StringVar()
        self.name_entry = tk.Entry(master, textvariable=self.name_entry_var)
        self.name_entry.pack(pady=10)

        # Entry for Password
        self.password_entry_label = tk.Label(master, text="Enter Password:")
        self.password_entry_label.pack(pady=5)
        self.password_entry_var = tk.StringVar()
        self.password_entry = tk.Entry(master, show="*", textvariable=self.password_entry_var)
        self.password_entry.pack(pady=10)

        # Login button
        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        # Back to Main Menu button
        self.back_button = tk.Button(master, text="Back to Main Menu", command=self.back_to_main_menu)
        self.back_button.pack(pady=10)

    def validate_login(self, name, password):
        # Simple login validation logic
        if name == "name" and password == "pass":
            return True
        else:
            return False

    def login(self):
        name = self.name_entry_var.get()
        password = self.password_entry_var.get()

        # Perform login validation using the method within the class
        if self.validate_login(name, password):
            self.master.destroy()
            exec(open("U_selectImage.py").read())
        else:
            self.master.destroy()
            exec(open("U_Wrong_Credentials.py").read())    

        self.master.destroy()
        # Replace the following line with the appropriate code for the next step after login
        # exec(open("NextStepAfterLogin.py").read())

    def back_to_main_menu(self):
        self.master.destroy()
        exec(open("U_Window_MainMenu.py").read())

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerWindow(root)
    root.mainloop()

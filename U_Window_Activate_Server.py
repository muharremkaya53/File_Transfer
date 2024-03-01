import tkinter as tk
from tkinter import messagebox
import subprocess
from U_GlobalVariables import IPv4IDofServer, portNumberOfServer

class ServerWindow:
    def __init__(self, master):
        self.master = master
        master.title("Server Control Panel")

        # Header
        self.header_label = tk.Label(master, text="START SERVER", font=("Helvetica", 16, "bold"))
        self.header_label.pack(pady=10)

        # Description
        self.description_label = tk.Label(master, text="This action will reset all ongoing client actions")
        self.description_label.pack(pady=5)

        # Entry for IPv4 address
        self.ipv4_entry_label = tk.Label(master, text="Enter IPv4 address:")
        self.ipv4_entry_label.pack(pady=5)
        # Set default value from U_GlobalVariables
        self.ipv4_entry_var = tk.StringVar(value=IPv4IDofServer)
        self.ipv4_entry = tk.Entry(master, textvariable=self.ipv4_entry_var)
        self.ipv4_entry.pack(pady=10)

        # Entry for Port
        self.port_entry_label = tk.Label(master, text="Enter Port Number:")
        self.port_entry_label.pack(pady=5)
        # Set default value from U_GlobalVariables
        self.port_entry_var = tk.StringVar(value=portNumberOfServer)
        self.port_entry = tk.Entry(master, textvariable=self.port_entry_var)
        self.port_entry.pack(pady=10)

        # Start Server button
        self.start_button = tk.Button(master, text="Start The Server", command=self.start_server)
        self.start_button.pack(pady=10)

        # Back to Main Menu button
        self.back_button = tk.Button(master, text="Back to Main Menu", command=self.back_to_main_menu)
        self.back_button.pack(pady=10)

    def start_server(self):
        ipv4_address = self.ipv4_entry_var.get()
        port = self.port_entry_var.get()

        if not ipv4_address or not port:
            messagebox.showerror("Error", "Please enter both IPv4 address and Port Number.")
            return

        try:
            # Update variables in U_GlobalVariables
            with open("U_GlobalVariables.py", "w") as global_var_file:
                global_var_file.write(f'IPv4IDofServer = "{ipv4_address}"\n')
                global_var_file.write(f'portNumberOfServer = "{port}"\n')
                global_var_file.write(f'dosyaAdi = "aExampleimage.jpg" \n')

            self.master.destroy()
            exec(open("U_Starter_Server.py").read())

        except Exception as e:
            messagebox.showerror("Error", f"Failed to start server: {str(e)}")

    def back_to_main_menu(self):
        self.master.destroy()
        exec(open("U_Window_MainMenu.py").read())

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerWindow(root)
    root.mainloop()

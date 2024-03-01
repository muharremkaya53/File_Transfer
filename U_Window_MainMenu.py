# main_script.py
import tkinter as tk
# we use this library to create the window
import socket
import ssl
import threading
import subprocess
# we use this library to run the other scripts
#  example#    subprocess.run(["python", "otherscript01.py"])


# from main_script import main_method 
# how to add a method from another script to this script
#  example#    main_method()

#this two lines opens the other window script and closes this one
#      self.master.destroy()
 #       exec(open("U_Window_Activate_Client.py").read())
from U_GlobalVariables import IPv4IDofServer, portNumberOfServer,dosyaAdi


class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Secure Transfer Protocol ")

        # Big Header
        self.header_label = tk.Label(master, text="      Choose Transfer Protocol      ", font=("Helvetica", 18, "bold"))
        self.header_label.pack(pady=20) 

        self.button1 = tk.Button(master, text="Start Client ", command=self.call_script1)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(master, text="Start Server ", command=self.call_script2)
        self.button2.pack(pady=10)

    def call_script1(self):
        #subprocess.run(["python", "U_Window_Activate_Client.py"])
        self.master.destroy()
        exec(open("U_Window_Activate_Client.py").read())

    def call_script2(self):
        self.master.destroy()
        exec(open("U_Window_Activate_Server.py").read())

      
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

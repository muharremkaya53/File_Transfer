import socket
import tkinter as tk
from tkinter import simpledialog

import hashlib
import subprocess

def send_credentials(name, password):
    try:
        data_to_hash = f"{name}{password}"
        hashed_data = hashlib.sha256(data_to_hash.encode('utf-8')).hexdigest()

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('192.168.0.119', 12345))

        credentials = f"Name: {name}, Hash: {hashed_data}"
        client_socket.send(credentials.encode('utf-8'))

        print(f"Credentials sent successfully.")

        # Receive the response from the server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

        # Close the connection
        client_socket.close()

        # Decide which script to run based on the server response
        if response.lower() == 'true':
            subprocess.run(['python', 'selectImage.py'])
        else:
            root.destroy()  # Close the Tkinter window
            exec(open("U_Wrong_Credentials.py").read())

    except (socket.error, Exception) as e:
        print(f"Error: {e}")

def get_user_input():
    name = tk.simpledialog.askstring("Input", "Enter your name:")  # Use tk.simpledialog
    password = tk.simpledialog.askstring("Input", "Enter your password:")
    
    if name and password:
        send_credentials(name, password)

root = tk.Tk()
root.title("Login Client")

input_button = tk.Button(root, text="Enter Credentials", command=get_user_input)
input_button.pack(pady=20)

# Properly handle the Tkinter window closing
root.protocol("WM_DELETE_WINDOW", root.destroy)

root.mainloop()

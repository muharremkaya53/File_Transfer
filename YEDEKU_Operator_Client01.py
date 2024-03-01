import os
import socket
import tkinter as tk
from tkinter import filedialog
import struct

def send_file(file_path):
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.0.119', 12345))

    # Pack file size as a 4-byte integer in big-endian byte order
    file_size_bytes = struct.pack('>I', file_size)
    client_socket.send(file_size_bytes)

    client_socket.send(file_name.encode('utf-8'))

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)

    print(f"File '{file_name}' sent successfully.")
    client_socket.close()

def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        send_file(file_path)

root = tk.Tk()
root.title("File Transfer Client")

choose_file_button = tk.Button(root, text="Choose File", command=choose_file)
choose_file_button.pack(pady=20)

send_button = tk.Button(root, text="Send", command=send_file)
send_button.pack(pady=20)

root.mainloop()

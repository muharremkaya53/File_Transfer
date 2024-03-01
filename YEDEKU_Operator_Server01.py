import socket
import os
import struct

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.0.119', 12345))
    server.listen(5)
    print("Server listening on port 12345")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        receive_file(client_socket)

def receive_file(client_socket):
    # Receive 4 bytes for file size
    file_size_bytes = client_socket.recv(4)
    file_size = struct.unpack('>I', file_size_bytes)[0]

    # Receive file name as raw binary data
    file_name_bytes = client_socket.recv(1024)
    file_name = file_name_bytes.decode('utf-8')  # Assuming file name was originally encoded in UTF-8

    with open(file_name, 'wb') as file:
        received_data = 0
        while received_data < file_size:
            data = client_socket.recv(1024)
            received_data += len(data)
            file.write(data)

    print(f"File '{file_name}' received successfully.")
    client_socket.close()

if __name__ == "__main__":
    start_server()

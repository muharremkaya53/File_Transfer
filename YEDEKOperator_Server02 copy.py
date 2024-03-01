import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.0.119', 12345))
    server.listen(5)
    print("Server listening on port 12345")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        receive_text(client_socket)

def receive_text(client_socket):
    message = client_socket.recv(1024).decode('utf-8')
    
    print(f"Received message: {message}")
    client_socket.close()

if __name__ == "__main__":
    start_server()

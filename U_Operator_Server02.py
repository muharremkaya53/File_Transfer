import socket
import hashlib
from U_HashLists import user_data

def validate_credentials(name, hashed_password):
    # Check if the given name is in the user_data hash list
    if name in user_data:
        # Retrieve the stored hash for the given name
        stored_hash = user_data[name]

        # Hash the provided password for comparison
        hashed_input_password = hashlib.sha256(hashed_password.encode('utf-8')).hexdigest()

        # Compare the hashed passwords
        if hashed_input_password == stored_hash:
            # If the hashes match, return True for successful validation
            return True
    # If the name is not in the hash list or the hashes don't match, return False
    return False


def handle_client(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received data: {data}")

    # Extract name and hashed password from the received data
    credentials = data.split(", ")
    name = credentials[0].split(": ")[1]
    hashed_password = credentials[1].split(": ")[1]

    # Validate the credentials
    validation_result = validate_credentials(name, hashed_password)

    # Send the validation result back to the client
    response = str(validation_result)
    client_socket.send(response.encode('utf-8'))

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.48', 555))
    server_socket.listen(1)
    print("Server listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()

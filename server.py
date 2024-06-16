import os
import time

class ServerSocket:
    def __init__(self, connection_file, request_file, response_file):
        self.connection_file = connection_file
        self.request_file = request_file
        self.response_file = response_file

        # Initialize files
        self._reset_files()

    def _reset_files(self):
        open(self.connection_file, 'w').close()
        open(self.request_file, 'w').close()
        open(self.response_file, 'w').close()

    def bind(self):
        print(f"Binding to files")

    def listen(self):
        print("Listening for connections...")

    def accept(self):
        print("Waiting for a connection...")
        while not os.path.getsize(self.connection_file):
            time.sleep(1)
        
        with open(self.connection_file, 'r') as file:
            client_address = file.read().strip()
        
        print(f"Accepted connection from {client_address}")
        return ClientHandler(self.request_file, self.response_file), client_address

class ClientHandler:
    def __init__(self, request_file, response_file):
        self.request_file = request_file
        self.response_file = response_file

    def recv(self, buffer_size):
        print("Waiting for data...")
        while not os.path.getsize(self.request_file):
            time.sleep(1)
        
        with open(self.request_file, 'r') as file:
            data = file.read(buffer_size)
        
        # Clear the request file after reading
        open(self.request_file, 'w').close()
        return data

    def send(self, data):
        print(f"Sending data: {data}")
        with open(self.response_file, 'w') as file:
            file.write(data)
        print(f"Data written to {self.response_file}")

    def close(self):
        print("Connection closed")

def handle_request(client_handler):
    request = client_handler.recv(1024)
    print(f"Received request: {request}")

    # Create HTTP response
    http_response = f"Salut, {request}!"
    client_handler.send(http_response)
    client_handler.close()

def run_server():
    connection_file = 'connection.txt'
    request_file = 'request.txt'
    response_file = 'response.txt'
    
    server_socket = ServerSocket(connection_file, request_file, response_file)
    server_socket.bind()
    server_socket.listen()

    while True:
        client_handler, client_address = server_socket.accept()
        handle_request(client_handler)

if __name__ == "__main__":
    run_server()

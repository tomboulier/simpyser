import os
import sys
import time

class ClientSocket:
    def __init__(self, connection_file, request_file, response_file):
        self.connection_file = connection_file
        self.request_file = request_file
        self.response_file = response_file

    def connect(self):
        print(f"Connecting to server")
        with open(self.connection_file, 'w') as file:
            file.write('client')
        
    def send(self, data):
        with open(self.request_file, 'w') as file:
            file.write(data)
        
    def recv(self, buffer_size):
        print("Waiting for response...")
        while not os.path.getsize(self.response_file):
            time.sleep(1)
        
        with open(self.response_file, 'r') as file:
            data = file.read(buffer_size)
        
        # Clear the response file after reading
        open(self.response_file, 'w').close()
        return data

    def close(self):
        print("Connection closed")

def start_client(name):
    connection_file = 'connection.txt'
    request_file = 'request.txt'
    response_file = 'response.txt'
    
    client_socket = ClientSocket(connection_file, request_file, response_file)
    client_socket.connect()

    client_socket.send(name)

    response = client_socket.recv(1024)
    print(f"Received response: {response}")

    client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    start_client(name)

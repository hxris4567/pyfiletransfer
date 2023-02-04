__author__ = "@hxris4567 on GitHub"

import socket
import struct
import os

SERVER_IP = '127.0.0.1' 
SERVER_PORT = 12345
DIRECTORY = "Received"

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))
    server.listen(1)
    print("Listening {}:{}".format(SERVER_IP, SERVER_PORT))

    while True:
        connection, client_address = server.accept()
        print("Received a connection from {}:{}".format(*client_address))

        file_name_len = struct.unpack("!i", connection.recv(4))[0]
        file_name = connection.recv(file_name_len).decode()
        file_size = struct.unpack("!i", connection.recv(4))[0]

        print("Received file '{}' with size {} bytes".format(file_name, file_size))

        if not os.path.exists(str(DIRECTORY)):
            os.makedirs(str(DIRECTORY))

        with open("Received/" + file_name, "wb") as f:
            while file_size > 0:
                chunk = connection.recv(4096)
                f.write(chunk)
                file_size -= len(chunk)

        print("File transfer complete")
        connection.close()

if __name__ == "__main__":
    run_server()

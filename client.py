__author__ = "@hxris4567 on GitHub"

import socket
import struct
import tkinter as tk
from tkinter import filedialog

SERVER_IP = "127.0.0.1"
SERVER_PORT = 12345

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    send_file(file_path)

def send_file(file_path):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))

    file_name = file_path.split("/")[-1].encode()
    file_name_len = len(file_name)
    client.sendall(struct.pack("!i", file_name_len))
    client.sendall(file_name)

    with open(file_path, "rb") as file:
        file_data = file.read()
        client.sendall(struct.pack("!i", len(file_data)))
        client.sendall(file_data)

select_file()

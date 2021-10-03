import socket
from tkinter import filedialog
s = socket.socket()
host = input(str("enter host addr:"))
port = 8034
s.connect((host, port))
print("connected....")

filename = input(str("enter filename:"))
file = open(filename, 'wb')
file_data = s.recv(4096)
file.write(file_data)
file.close()
print("file received.......")
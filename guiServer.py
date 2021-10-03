import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import scrolledtext
import socket
import sys
import os

def selectFile():
    files = fd.askopenfilenames(parent=root, title="Choose a file")
    # lab2.config(text=files)

def sendFile():
    pass

def receiveFile():
    pass

soc = socket.socket()

root = tk.Tk()
root.geometry("480x370")
root.title("File Sharing")

# frame1 = tk.Frame(root, width=400, height=400,bg="pink")
# frame1.grid()
# frame1.pack()

# btnSend = tk.Button(frame1, text="Send", width=30, height=2, command=sendFile)
# btnSend.grid(row=0, column=0)

# btnReceive = tk.Button(frame1, text="Receive", width=30, height=2, command=receiveFile)
# btnReceive.grid(row=0, column=1)

frame2 = tk.Frame(root, width=400, height=400, bg="pink")
frame2.grid(padx=0, pady=0)
frame2.pack()

lab1 = tk.Label(frame2, text="Connection ID", width=20, height=3, bg="red")
lab1.grid(row=0, column=0, padx=0)

lab2 = tk.Label(frame2, text=socket.gethostname(), width=20, height=3, bg="yellow")
lab2.grid(row=0, column=1, padx=0)

filename = scrolledtext.ScrolledText(frame2, width=50, height=10, bg="orange")
# filename.insert("this is a string","")
# filename.place(width=500, height=500)
filename.grid(row=1, column=0, padx=1, columnspan=2)

btn = tk.Button(frame2, text="Browse", command=selectFile, width=20, height=2)
# btn.pack()
btn.grid(row=3, column=0, padx=1)

root.mainloop()

# import socket
# from tkinter import filedialog
# s = socket.socket()
# host = socket.gethostname()
# port = 8034
# s.bind((host, port))
# s.listen()
# print("Wating for connection...")
# conn, addr = s.accept()
# print(addr,"Connected to server")
# filename = input(str("Enter filename: "))
# file = open(filename, 'rb')
# file_data = file.read(4096)
# conn.send(file_data)
# print("data sent successfully")
# file.close()
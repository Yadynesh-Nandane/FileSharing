import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import scrolledtext
import socket
import sys
import os

def selectFile():
    files = fd.askopenfilenames(parent=root, title="Choose a file")
    lab2.config(text=files)

soc = socket.socket()

root = tk.Tk()
root.geometry("480x370")
root.title("File Sharing")

frame = tk.Frame(root, width=400, height=400, bg="pink")
frame.grid(padx=0.2, pady=1)
# frame.pack()

lab1 = tk.Label(frame, text="Connection ID", width=20, height=3, bg="red")
lab1.grid(row=0, column=0, padx=0)

lab2 = tk.Label(frame, text=socket.gethostname(), width=20, height=3, bg="yellow")
lab2.grid(row=0, column=1, padx=0)

filename = scrolledtext.ScrolledText(frame, width=50, height=10, bg="orange")
# filename.insert("this is a string","")
# filename.place(width=500, height=500)
filename.grid(row=1, column=0, padx=1, columnspan=2)

btn = tk.Button(frame, text="Browse", command=selectFile, width=20, height=2)
# btn.pack()
btn.grid(row=3, column=0, padx=1)

root.mainloop()
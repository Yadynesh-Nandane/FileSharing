import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import Image, ImageTk
import socket
import sys
import os

def mainWindow():
    splash_screen.destroy()

    def sendFile():
        # messagebox.showinfo("showinfo", "This is just a Information")
        frame2.pack(fill="both", expand=1)
        frame1.forget()

    def receiveFile():
        pass

    def selectFile():
        files = fd.askopenfilenames(parent=root, title="Choose a file")
        # lab2.config(text=files)
    

    root = tk.Tk()

    width = 480
    height = 370
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.title("File Sharing")
    # root.resizable(False, False)

    frame1 = tk.Frame(root, bg="pink", width=400, height=370)
    frame1.pack(fill="both")

    img = Image.open("icon.jpg").resize((400, 370), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    label1 = Label(root, image = photo, bg="lightblue", font=("", 30))
    label1.place(x=300, y=120, anchor="center")

    btnSend = tk.Button(frame1, text="Send", width=20, height=2, command=sendFile)
    btnSend.grid(row=1, column=0)

    btnReceive = tk.Button(frame1, text="Receive", width=20, height=2, command=receiveFile)
    btnReceive.grid(row=1, column=1)

    btnChat = tk.Button(frame1, text="Chat", width=20, height=2, command=receiveFile)
    btnChat.grid(row=1, column=2)

    frame2 = tk.Frame(root, width=400, height=400, bg="pink")

    lab1 = tk.Label(frame2, text="Connection ID", width=20, height=3, bg="red")
    lab1.grid(row=0, column=0, padx=0)

    lab2 = tk.Label(frame2, text=socket.gethostname(), width=20, height=3, bg="yellow")
    lab2.grid(row=0, column=1, padx=0)

    filename = scrolledtext.ScrolledText(frame2, width=50, height=10, bg="orange")
    # filename.insert("this is a string","")
    filename.grid(row=1, column=0, padx=1, columnspan=2)

    btn = tk.Button(frame2, text="Browse", command=selectFile, width=20, height=2)
    # btn.pack()
    btn.grid(row=3, column=0, padx=1)
    
    root.mainloop()


splash_screen = Tk()
width = 600
height = 300
screen_width = splash_screen.winfo_screenwidth()
screen_height = splash_screen.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

splash_screen.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
splash_screen.config(bg="lightblue")

img = Image.open("icon.jpg").resize((width, height), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(img)

label1 = Label(splash_screen, image = photo, bg="lightblue", font=("", 30))
label1.place(x=300, y=120, anchor="center")

splash_screen.after(5000, mainWindow)
splash_screen.overrideredirect(True)

mainloop()

# import socket
# from tkinter import filedialog
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
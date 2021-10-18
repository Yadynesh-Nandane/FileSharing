"""
Author    : Wandering Minds
Date      :
Email_ID  : wanderingmindsprojectsolutions@gmail.com
Contact No: 9619682473
Project   : Youtube Transcript Summarizer
Files to Submit: .exe, .py

"""
from tkinter import *
import tkinter as tk
from tkinter import font

def mainWindow():
    splash_screen.destroy()

    def videosFrame():
        framevideos.pack()
        framemain.forget()

    def moviesFrame():
        framemovies.pack()
        framemain.forget()

    def videosbackfun():
        framevideos.forget()
        framemain.pack()

    def moviesbackfun():
        framemovies.forget()
        framemain.pack()

    root = tk.Tk()
    root.geometry("700x550")
    root.resizable(False, False)

    framemain = tk.Frame(root, bg="grey")
    framemain.pack(fill=BOTH, expand=True)

    label1 = Label(framemain, text="Youtube Transcript Summarizer", width=100, height= 2, bg="orange")
    label1.config(font=("", 30))
    label1.pack(pady=10)

    subframe = tk.Frame(framemain, width=670, height=400, bg="grey")
    subframe.pack(pady=20)
    subframe.propagate(0)

    devLabel = Label(subframe, text="Developed By: - Saloni Morya & Pradnya Pophale", width=100, height= 2, bg="#9c9e9c", fg="black")
    devLabel.config(font=("", 15))
    devLabel.pack()

    btnVideos = tk.Button(subframe, text="Videos", width=18, height=2, bg="red", command=videosFrame)
    btnVideos.config(font=("", 23))
    btnVideos.pack(pady=40)

    btnMovies = tk.Button(subframe, text="Movies", width=18, height=2, bg="red", command=moviesFrame)
    btnMovies.config(font=("", 23))
    btnMovies.pack(pady=10)



    # label1 = Label(frameshorts, text="Select Your Video frameshorts", width=100, height= 2, bg="orange")
    # label1.config(font=("", 30))
    # label1.pack(pady=10)

    framevideos = tk.Frame(root, width=700, height=570, bg="#9c9e9c")
    framevideos.pack()
    framevideos.pack_propagate(0)

    label1 = Label(framevideos, text="Youtube Video Summarizer", width=30, height= 2, bg="orange")
    label1.config(font=("", 28))
    label1.pack(side=TOP)

    videosSubFrame = tk.Frame(framevideos, bg="white")
    videosSubFrame.grid()
    # videosSubFrame.pack_propagate(0)
    # width=700, height=570,

    linkLabel1 = Label(videosSubFrame, text="Youtube Link", width=30, bg="#9c9e9c")
    linkLabel1.config(font=("", 15))
    linkLabel1.grid(row=0, column=0)

    youtubeLink = tk.Text(videosSubFrame, width=40, height=1)
    youtubeLink.grid(row=1, column=1, columnspan=3)

    sentimentBtn = tk.Button(videosSubFrame, text="Sentiment Analysis", width=18, height=2, bg="red", command=moviesFrame)
    sentimentBtn.config(font=("", 23))
    sentimentBtn.pack(side=LEFT)


    # videosBack = tk.Button(framevideos, text="Back", width=18, height=2, bg="red", command=videosbackfun)
    # videosBack.config(font=("", 23))
    # videosBack.pack(pady=10)

    # framemovies = tk.Frame(root, width=500, height=500, bg="#9c9e9c")
    # # framemovies.pack()
    # framemovies.pack_propagate(0)

    # label1 = Label(framemovies, text="Select Your Video framemovies", width=100, height= 2, bg="orange")
    # label1.config(font=("", 30))
    # label1.pack(pady=10)

    # moviesBack = tk.Button(framemovies, text="Back", width=18, height=2, bg="red", command=moviesbackfun)
    # moviesBack.config(font=("", 23))
    # moviesBack.pack(pady=10)
    #9c9e9c



    root.mainloop()

splash_screen = Tk()
splash_screen.geometry("400x400")
splash_screen.overrideredirect(True)

greet = Label(splash_screen, text="youtube transcript", height= 5)
greet.config(font=("", 30))
greet.pack()

splash_screen.after(100, mainWindow)

mainloop()
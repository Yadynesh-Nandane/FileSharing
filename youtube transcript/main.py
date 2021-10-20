"""
Author              : Wandering Minds
Date                :
Email_ID            : wanderingmindsprojectsolutions@gmail.com
Contact No          : 9619682473
Project             : Youtube Transcript Summarizer
Files to Submit     : .exe, .py
"""

from tkinter import *
import tkinter as tk
from tkinter import font
from typing import Collection

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
    root.geometry("780x630")
    root.resizable(False, False)


    # Main Window Code
    framemain = tk.Frame(root, width=780, height=630, bg="grey")
    framemain.pack(fill=BOTH, expand=True)
    framemain.pack_propagate(0)

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


    #------------------------------ Videos Window Code --------------------------------------------------------------

    framevideos = tk.Frame(root, width=780, height=630, bg="#9c9e9c")
    framevideos.pack_propagate(0)

    label1 = Label(framevideos, text="Youtube Video Summarizer", width=34, height= 2, bg="orange")
    label1.config(font=("", 28))
    label1.pack(side=TOP)

    videosSubFrame = tk.Frame(framevideos, bg="lightblue")
    videosSubFrame.pack(fill=BOTH, expand=True, padx=10)

    linkLabel1 = Label(videosSubFrame, text="Youtube Link", width=20, height=1, bg="#9c9e9c")
    linkLabel1.config(font=("", 15))
    linkLabel1.grid(row=0, column=0, columnspan=1)

    youtubeLink = tk.Text(videosSubFrame, width=67, height=2)
    youtubeLink.config(font=("", 10))
    youtubeLink.grid(row=0, column=1, columnspan=2)

    sentimentBtn = tk.Button(videosSubFrame, text="Sentiment Analysis", width=20, height=1, bg="red", command=moviesFrame)
    sentimentBtn.config(font=("", 15))
    sentimentBtn.grid(row=2, column=0)

    summaryBtn = tk.Button(videosSubFrame, text="Generate Summary", width=20, height=1, bg="red", command=moviesFrame)
    summaryBtn.config(font=("", 15))
    summaryBtn.grid(row=2, column=2, columnspan=1)

    sentimentFrame = tk.Frame(videosSubFrame, width=30, height=2, bg="pink")
    sentimentFrame.grid(row=3, column=0, columnspan=3) 

    sentimemtPValLabel = Label(sentimentFrame, text="|Positive|", width=20, height=1, bg="#9c9e9c")
    sentimemtPValLabel.config(font=("", 15))
    sentimemtPValLabel.grid(row=0, column=0, columnspan=1)

    sentimemtNeValLabel = Label(sentimentFrame, text="|Negative|", width=22, height=1, bg="#9c9e9c")
    sentimemtNeValLabel.config(font=("", 15))
    sentimemtNeValLabel.grid(row=0, column=1, columnspan=1)

    sentimemtPValLabel = Label(sentimentFrame, text="|Neutral|", width=20, height=1, bg="#9c9e9c")
    sentimemtPValLabel.config(font=("", 15))
    sentimemtPValLabel.grid(row=0, column=2, columnspan=1)

    sentimemtPValLabel = Label(videosSubFrame, text="|Neutral|", width=20, height=1, bg="#9c9e9c")
    sentimemtPValLabel.config(font=("", 15))
    sentimemtPValLabel.grid(row=4, column=0, columnspan=1)

    summary = tk.Text(videosSubFrame, width=88, height=20, bg="yellow")
    summary.grid(row=5, column=0, rowspan=2, columnspan=3)

    summaryBtn = tk.Button(videosSubFrame, text="Back", width=20, height=1, bg="red", command=videosbackfun)
    summaryBtn.config(font=("", 15))
    summaryBtn.grid(row=7, column=0, columnspan=1)

    summaryBtn = tk.Button(videosSubFrame, text="Save as PDF", width=20, height=1, bg="red", command=moviesFrame)
    summaryBtn.config(font=("", 15))
    summaryBtn.grid(row=7, column=2, columnspan=1)


    #---------------------------------- Movies Window Code ----------------------------------------------------------------------------
    
    framemovies = tk.Frame(root, width=780, height=630, bg="#9c9e9c")
    framemovies.pack_propagate(0)

    label1 = Label(framemovies, text="Youtube Movies Summarizer", width=34, height= 2, bg="orange")
    label1.config(font=("", 28))
    label1.pack(side=TOP)

    moviesSubFrame = tk.Frame(framemovies, bg="lightblue")
    moviesSubFrame.pack(fill=BOTH, expand=True, padx=10)

    linkLabel1 = Label(moviesSubFrame, text="Youtube Link", width=20, height=1, bg="#9c9e9c")
    linkLabel1.config(font=("", 15))
    linkLabel1.grid(row=0, column=0, columnspan=1)

    youtubeLink = tk.Text(moviesSubFrame, width=67, height=2)
    youtubeLink.config(font=("", 10))
    youtubeLink.grid(row=0, column=1, columnspan=2)

    sentimentBtn = tk.Button(moviesSubFrame, text="Sentiment Analysis", width=20, height=1, bg="red", command=moviesFrame)
    sentimentBtn.config(font=("", 15))
    sentimentBtn.grid(row=2, column=0)

    summaryBtn = tk.Button(moviesSubFrame, text="Generate Summary", width=20, height=1, bg="red", command=moviesFrame)
    summaryBtn.config(font=("", 15))
    summaryBtn.grid(row=2, column=2, columnspan=1)

    msentimentFrame = tk.Frame(moviesSubFrame, width=30, height=2, bg="pink")
    msentimentFrame.grid(row=3, column=0, columnspan=3) 

    sentimemtPValLabel = Label(msentimentFrame, text="|Positive|", width=20, height=1, bg="#9c9e9c")
    sentimemtPValLabel.config(font=("", 15))
    sentimemtPValLabel.grid(row=0, column=0, columnspan=1)

    sentimemtNeValLabel = Label(msentimentFrame, text="|Negative|", width=22, height=1, bg="#9c9e9c")
    sentimemtNeValLabel.config(font=("", 15))
    sentimemtNeValLabel.grid(row=0, column=1, columnspan=1)

    sentimemtPValLabel = Label(msentimentFrame, text="|Neutral|", width=20, height=1, bg="#9c9e9c")
    sentimemtPValLabel.config(font=("", 15))
    sentimemtPValLabel.grid(row=0, column=2, columnspan=1)

    sentimemtPValLabel = Label(moviesSubFrame, text="|Neutral|", width=20, height=1, bg="#9c9e9c")
    sentimemtPValLabel.config(font=("", 15))
    sentimemtPValLabel.grid(row=4, column=0, columnspan=1)

    summary = tk.Text(moviesSubFrame, width=88, height=20, bg="yellow")
    summary.grid(row=5, column=0, rowspan=2, columnspan=3)

    summaryBtn = tk.Button(moviesSubFrame, text="Back", width=20, height=1, bg="red", command=moviesbackfun)
    summaryBtn.config(font=("", 15))
    summaryBtn.grid(row=7, column=0, columnspan=1)

    summaryBtn = tk.Button(moviesSubFrame, text="Save as PDF", width=20, height=1, bg="red", command=moviesFrame)
    summaryBtn.config(font=("", 15))
    summaryBtn.grid(row=7, column=2, columnspan=1)

    root.mainloop()


#------------------------------------------ Splash Screen Code ---------------------------------------------------
splash_screen = Tk()
splash_screen.geometry("780x630")
splash_screen.overrideredirect(True)

greet = Label(splash_screen, text="Youtube Transcript", height= 5)
greet.config(font=("", 30))
greet.pack()

splash_screen.after(3000, mainWindow)

mainloop()
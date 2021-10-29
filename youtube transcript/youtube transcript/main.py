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
from PIL import Image
import transformers
import torch
import youtube_transcript_api
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo


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
    

    def sentimentAnalysis():
        pass

    def generateSummary():
        youtube_video = youtubeLink.get(1.0, "end-1c")
        video_id = youtube_video.split("=")[1]
        summary.config(text=video_id)

    def saveAsPDF():
        pass


    root = tk.Tk()
    width = 780
    height = 630

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    root.title("Transcript Summarizer")
    root.iconbitmap(r'youtube.ico')
    root.resizable(False, False)


    #----------------------------------------------------- Main Window Code----------------------------------------------------------------

    framemain = tk.Frame(root, width=780, height=630, bg="#D8D8D8")
    framemain.pack(fill=BOTH, expand=True)
    framemain.pack_propagate(0)

    label1 = Label(framemain, text="Youtube Transcript Summarizer", width=100, height= 2, bg="#E51F24")
    label1.config(font=("", 30))
    label1.pack()

    subframe = tk.Frame(framemain, width=670, height=400, bg="#D8D8D8")
    subframe.pack(pady=20)
    subframe.propagate(0)

    btnVideos = tk.Button(subframe, text="Videos", width=18, height=2, bg="red", command=videosFrame)
    btnVideos.config(font=("", 23))
    btnVideos.pack(pady=40)

    btnMovies = tk.Button(subframe, text="Movies", width=18, height=2, bg="red", command=moviesFrame)
    btnMovies.config(font=("", 23))
    btnMovies.pack(pady=10)

    greetLabel = tk.Label(framemain, text="Developed By:- Pradnya & Saloni\nProj. Guide:- Shajil Sir", width=100, bg="#D8D8D8")
    greetLabel.config(font=("", 10))
    greetLabel.pack(pady=6)


    #------------------------------ Videos Window Code --------------------------------------------------------------

    framevideos = tk.Frame(root, width=780, height=630, bg="#D8D8D8")
    framevideos.pack_propagate(0)

    label1 = Label(framevideos, text="Youtube Video Summarizer", width=34, height= 2, bg="#E51F24")
    label1.config(font=("", 28))
    label1.pack(side=TOP)

    videosSubFrame = tk.Frame(framevideos, bg="#D8D8D8")
    videosSubFrame.pack(fill=BOTH, expand=True, padx=10)

    linkLabel1 = Label(videosSubFrame, text="Youtube Link:-", width=20, height=1, bg="#D8D8D8")
    linkLabel1.config(font=("", 15))
    linkLabel1.grid(row=0, column=0, columnspan=1)

    youtubeLink = tk.Text(videosSubFrame, width=67, height=2, bg="#EEECE1")
    youtubeLink.config(font=("", 10))
    youtubeLink.grid(row=0, column=1, columnspan=2)

    sentimentBtn = tk.Button(videosSubFrame, text="Sentiment Analysis", width=20, height=1, bg="#D99594", command=sentimentAnalysis)
    sentimentBtn.config(font=("", 15))
    sentimentBtn.grid(row=2, column=0, columnspan=1)

    summaryBtn = tk.Button(videosSubFrame, text="Generate Summary", width=20, height=1, bg="#D99594", command=generateSummary)
    summaryBtn.config(font=("", 15))
    summaryBtn.grid(row=2, column=2, columnspan=1)

    sentimentFrame = tk.Frame(videosSubFrame, width=30, height=2, bg="#F2DBDB", highlightbackground="black", highlightthickness=2)
    sentimentFrame.grid(row=3, column=0, columnspan=3) 

    sentimemtPValLabel = Label(sentimentFrame, text="|Positive|", width=20, height=1, bg="#F2DBDB")
    sentimemtPValLabel.config(font=("", 15))
    sentimemtPValLabel.grid(row=0, column=0, columnspan=1)

    sentimemtNeValLabel = Label(sentimentFrame, text="|Negative|", width=22, height=1, bg="#F2DBDB")
    sentimemtNeValLabel.config(font=("", 15))
    sentimemtNeValLabel.grid(row=0, column=1, columnspan=1)

    sentimemtPValLabel = Label(sentimentFrame, text="|Neutral|", width=20, height=1, bg="#F2DBDB")
    sentimemtPValLabel.config(font=("", 15))
    sentimemtPValLabel.grid(row=0, column=2, columnspan=1)


    countFrame = tk.Frame(videosSubFrame, width=50, height=2, bg="#F2DBDB", highlightbackground="black", highlightthickness=2)
    countFrame.grid(row=4, column=0, columnspan=3) 

    transcriptValLabel = Label(countFrame, text="Transcript Word Count:- 2450", width=25, height=1, bg="#F2DBDB")
    transcriptValLabel.config(font=("", 15), padx = 10)
    transcriptValLabel.grid(row=0, column=0, columnspan=1)

    sentimemtPValLabel = Label(countFrame, text="Summary Word Count:- 990", width=25, height=1, bg="#F2DBDB")
    sentimemtPValLabel.config(font=("", 15))
    sentimemtPValLabel.grid(row=0, column=2, columnspan=1)

    summary = tk.Label(videosSubFrame, width=88, height=20, bg="#EEECE1", state=DISABLED)
    summary.grid(row=5, column=0, rowspan=2, columnspan=3)

    summaryBtn = tk.Button(videosSubFrame, text="Back", width=20, height=1, bg="#D99594", command=videosbackfun)
    summaryBtn.config(font=("", 15))
    summaryBtn.grid(row=7, column=0, columnspan=1)

    summaryBtn = tk.Button(videosSubFrame, text="Save as PDF", width=20, height=1, bg="#D99594", command=saveAsPDF)
    summaryBtn.config(font=("", 15))
    summaryBtn.grid(row=7, column=2, columnspan=1)


    #---------------------------------- Movies Window Code ----------------------------------------------------------------------------
    
    framemovies = tk.Frame(root, width=780, height=630, bg="#D8D8D8")
    framemovies.pack_propagate(0)

    mlabel1 = Label(framemovies, text="Youtube Movies Summarizer", width=34, height= 2, bg="#E51F24")
    mlabel1.config(font=("", 28))
    mlabel1.pack(side=TOP)

    moviesSubFrame = tk.Frame(framemovies, bg="#D8D8D8")
    moviesSubFrame.pack(fill=BOTH, expand=True, padx=10)

    mlinkLabel1 = Label(moviesSubFrame, text="Youtube Link", width=20, height=1, bg="#D8D8D8")
    mlinkLabel1.config(font=("", 15))
    mlinkLabel1.grid(row=0, column=0, columnspan=1)

    myoutubeLink = tk.Text(moviesSubFrame, width=67, height=2, bg="#EEECE1")
    myoutubeLink.config(font=("", 10))
    myoutubeLink.grid(row=0, column=1, columnspan=2)

    msentimentBtn = tk.Button(moviesSubFrame, text="Sentiment Analysis", width=20, height=1, bg="#D99594", command=sentimentAnalysis)
    msentimentBtn.config(font=("", 15))
    msentimentBtn.grid(row=2, column=0, columnspan=1)

    msummaryBtn = tk.Button(moviesSubFrame, text="Generate Summary", width=20, height=1, bg="#D99594", command=generateSummary)
    msummaryBtn.config(font=("", 15))
    msummaryBtn.grid(row=2, column=2, columnspan=1)

    msentimentFrame = tk.Frame(moviesSubFrame, width=30, height=2, bg="#F2DBDB", highlightbackground="black", highlightthickness=2)
    msentimentFrame.grid(row=3, column=0, columnspan=3) 

    msentimemtPValLabel = Label(msentimentFrame, text="|Positive|", width=20, height=1, bg="#F2DBDB")
    msentimemtPValLabel.config(font=("", 15))
    msentimemtPValLabel.grid(row=0, column=0, columnspan=1)

    msentimemtNeValLabel = Label(msentimentFrame, text="|Negative|", width=22, height=1, bg="#F2DBDB")
    msentimemtNeValLabel.config(font=("", 15))
    msentimemtNeValLabel.grid(row=0, column=1, columnspan=1)

    msentimemtPValLabel = Label(msentimentFrame, text="|Neutral|", width=20, height=1, bg="#F2DBDB")
    msentimemtPValLabel.config(font=("", 15))
    msentimemtPValLabel.grid(row=0, column=2, columnspan=1)

    mcountFrame = tk.Frame(moviesSubFrame, width=50, height=2, bg="#F2DBDB", highlightbackground="black", highlightthickness=2)
    mcountFrame.grid(row=4, column=0, columnspan=3) 

    mtranscriptValLabel = Label(mcountFrame, text="Transcript Word Count:- 2450", width=25, height=1, bg="#F2DBDB")
    mtranscriptValLabel.config(font=("", 15), padx = 10)
    mtranscriptValLabel.grid(row=0, column=0, columnspan=1)

    msentimemtPValLabel = Label(mcountFrame, text="Summary Word Count:- 990", width=25, height=1, bg="#F2DBDB")
    msentimemtPValLabel.config(font=("", 15))
    msentimemtPValLabel.grid(row=0, column=2, columnspan=1)

    msummary = tk.Text(moviesSubFrame, width=88, height=20, bg="#EEECE1", state=DISABLED)
    msummary.grid(row=5, column=0, rowspan=2, columnspan=3)

    msummaryBtn = tk.Button(moviesSubFrame, text="Back", width=20, height=1, bg="#D99594", command=moviesbackfun)
    msummaryBtn.config(font=("", 15))
    msummaryBtn.grid(row=7, column=0, columnspan=1)

    msummarysaveBtn = tk.Button(moviesSubFrame, text="Save as PDF", width=20, height=1, bg="#D99594", command=saveAsPDF)
    msummarysaveBtn.config(font=("", 15))
    msummarysaveBtn.grid(row=7, column=2, columnspan=1)

    root.mainloop()


#------------------------------------------ Splash Screen Code ---------------------------------------------------

splash_screen = Tk()

width = 780
height = 630

screen_width = splash_screen.winfo_screenwidth()
screen_height = splash_screen.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

splash_screen.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
splash_screen.overrideredirect(True)

img = PhotoImage(file = "Transcript_Summarizer.png")

devLabel = Label(splash_screen, image = img, fg="black")
devLabel.config(font=("", 15))
devLabel.pack()

splash_screen.after(100, mainWindow)

# width = 600
# height = 300
# screen_width = splash_screen.winfo_screenwidth()
# screen_height = splash_screen.winfo_screenheight()
# x = (screen_width / 2) - (width / 2)
# y = (screen_height / 2) - (height / 2)

# splash_screen.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
# splash_screen.config(bg="lightblue")

# img = Image.open("icon.jpg").resize((width, height), Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(img)

# label1 = Label(splash_screen, image = photo, bg="lightblue", font=("", 30))
# label1.place(x=300, y=120, anchor="center")

# splash_screen.after(5000, mainWindow)
# splash_screen.overrideredirect(True)

mainloop()
from tkinter import *
import tkinter as tk
from tkinter import font

def mainWindow():
    splash_screen.destroy()

    def shortsFrame():
        frameshorts.pack()
        framemain.forget()

    def videosFrame():
        framevideos.pack()
        framemain.forget()

    def moviesFrame():
        framemovies.pack()
        framemain.forget()

    def shortsbackfun():
        frameshorts.forget()
        framemain.pack()

    def videosbackfun():
        framevideos.forget()
        framemain.pack()

    def moviesbackfun():
        framemovies.forget()
        framemain.pack()

    root = tk.Tk()
    root.geometry("500x500")

    framemain = tk.Frame(root, width=500, height=500, bg="grey")
    framemain.pack()
    framemain.pack_propagate(0)

    label1 = Label(framemain, text="Select Your Video Category", width=100, height= 2, bg="orange")
    label1.config(font=("", 30))
    label1.pack(pady=10)

    btnShorts = tk.Button(framemain, text="Shorts", width=18, height=2, bg="red", command=shortsFrame)
    btnShorts.config(font=("", 23))
    btnShorts.pack(pady=10)

    btnVideos = tk.Button(framemain, text="Videos", width=18, height=2, bg="red", command=videosFrame)
    btnVideos.config(font=("", 23))
    btnVideos.pack(pady=10)

    btnMovies = tk.Button(framemain, text="Movies", width=18, height=2, bg="red", command=moviesFrame)
    btnMovies.config(font=("", 23))
    btnMovies.pack(pady=10)

    frameshorts = tk.Frame(root, width=500, height=500, bg="grey")
    # frameshorts.pack()
    frameshorts.pack_propagate(0)

    label1 = Label(frameshorts, text="Select Your Video frameshorts", width=100, height= 2, bg="orange")
    label1.config(font=("", 30))
    label1.pack(pady=10)

    shortsBack = tk.Button(frameshorts, text="Back", width=18, height=2, bg="red", command=shortsbackfun)
    shortsBack.config(font=("", 23))
    shortsBack.pack(pady=10)

    framevideos = tk.Frame(root, width=500, height=500, bg="grey")
    # framevideos.pack()
    framevideos.pack_propagate(0)

    label1 = Label(framevideos, text="Select Your Video framevideos", width=100, height= 2, bg="orange")
    label1.config(font=("", 30))
    label1.pack(pady=10)

    videosBack = tk.Button(framevideos, text="Back", width=18, height=2, bg="red", command=videosbackfun)
    videosBack.config(font=("", 23))
    videosBack.pack(pady=10)

    framemovies = tk.Frame(root, width=500, height=500, bg="grey")
    # framemovies.pack()
    framemovies.pack_propagate(0)

    label1 = Label(framemovies, text="Select Your Video framemovies", width=100, height= 2, bg="orange")
    label1.config(font=("", 30))
    label1.pack(pady=10)

    moviesBack = tk.Button(framemovies, text="Back", width=18, height=2, bg="red", command=moviesbackfun)
    moviesBack.config(font=("", 23))
    moviesBack.pack(pady=10)
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
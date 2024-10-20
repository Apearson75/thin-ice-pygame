import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.filedialog
from game import main
from levelMaker import editor

window = tk.Tk("Thin Ice Launcher")
window.geometry("300x300")
levelFile = None

def fileCallback():
    global levelFile
    levelFile = askopenfilename(filetypes=[("JSON Files", "*.json")])
    messagebox.showinfo("Opened File", f"Opened file successfully: {levelFile}")

def playCallback():
    score, result = main(levelFile)
    messagebox.showinfo(result, f"Your score is: {score}")

def editorCallback():
    editor(levelFile)
    messagebox.showinfo("Editor", f"File saved to {levelFile}")

fileButton = tk.Button(text="Open File", command=fileCallback)
fileButton.pack()
fileButton.place(relx=0.5, rely=.1, anchor=CENTER)

playButton = tk.Button(text="Play", command=playCallback)
playButton.pack()
playButton.place(relx=0.2, rely=0.5)

editorButton = tk.Button(text="Edit", command=editorCallback)
editorButton.pack()
editorButton.place(relx=0.8, rely=0.5)
window.mainloop()
import tkinter as tk
import json
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.filedialog
from game import main
from levelMaker import editor

window = tk.Tk("Thin Ice Launcher")
window.title("Thin Ice Launcher")
window.geometry("300x300")
levelFile = None

def createLevel():
    x = 20
    y = 20
    grid = []
    for i in range(x):
        for j in range(y):
            sType = "Ice"
            if i == 1 and j == 1:
                sType = "Spawn"
            square = {
                "i": i,
                "j": j,
                "x": i * 600/x,
                "y": j * 600/y,
                "size": (600/x, 600/y),
                "rectValue": (i * 600/x, j * 600/y, 600/x, 600/y),
                "type": sType
            }
            grid.append(square)
    return grid

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

def createFileCallback():
    global levelFile
    saveAsFile = asksaveasfilename(filetypes=[("JSON Files", "*.json")], defaultextension=".json")
    with open(saveAsFile, "w") as w:
        json.dump(createLevel(), w)
    levelFile = saveAsFile
    messagebox.showinfo("Created Level", f"Created Level: {saveAsFile}")

fileButton = tk.Button(text="Open File", command=fileCallback)
fileButton.pack()
fileButton.place(relx=0.5, rely=.1, anchor=CENTER)

playButton = tk.Button(text="Play", command=playCallback)
playButton.pack()
playButton.place(relx=0.2, rely=0.5)

editorButton = tk.Button(text="Edit", command=editorCallback)
editorButton.pack()
editorButton.place(relx=0.8, rely=0.5)

createButton = tk.Button(text="Create Level", command=createFileCallback)
createButton.pack()
createButton.place(relx=0.5, rely=.9, anchor=CENTER)
window.mainloop()
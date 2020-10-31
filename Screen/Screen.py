import tkinter as tk
from PIL import Image, ImageTk
import os

class MainWindow(tk.Frame):
    TITLE = "Exodus Game Engine"
    def __init__(self, master = None, width = 800, height = 600, GameTitle = None):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height
        os.chdir('/Users/andreasevensen/Documents/GitHub/Exodus/Screen')
        self.initializewindow()

    def initializewindow(self):

        self.master.geometry(f'{self.width}x{self.height}')

        self.master.title(self.TITLE)
        def donothing():
            label = tk.Label(self.master, text = "You pressed").pack()
            pass

        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar)


#851 × 422
#/Users/andreasevensen/Documents/GitHub/Exodus/Screen

root = tk.Tk()
app = MainWindow(root)
app.mainloop()

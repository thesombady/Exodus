import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Frame):
    """ Makes a two-dimensional image """
    
    Width = 500
    Height = 500
    #Class variables that can be changed over time.

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.geometry(f'{self.Width}x{self.Height}')

root = tk.Tk()
app = Application(root)
app.mainloop()
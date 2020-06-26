import tkinter as tk
from PIL import Image, ImageTk

class MainWindow(tk.Frame):
    TITLE = "Exodus Game Engine"
    def __init__(self, master = None, width = 1000, height = 800, GameTitle = None):
        super().__init__(master)
        self.master = master
        self.width = width
        self.height = height
        self.master.geometry(f'{self.width}x{self.height}')
        self.master.title(self.TITLE)
        Canvas = tk.Canvas(self.master, width = 841, height = 422, bg = 'blue')
        Canvas.pack()
        img = ImageTk('Exodus.jpg')
        Canvas.create_image(self.master, width = 841, height = 422, image=img)

#851 × 422


root = tk.Tk()
app = MainWindow(root)
app.mainloop()

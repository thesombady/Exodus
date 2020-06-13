import Vector as vc
import tkinter as tk


class Application(tk.Frame):

    title = None
    width = 500
    height = 500

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.master.title(self.title)
        self.master.geometry(f'{self.width}x{self.height}')
        self.drawcanvas()
    
    def drawcanvas(self):
        self.canvas = tk.Canvas(self.master, width = self.width,
            height = self.height, bg = 'blue')
        self.canvas.pack()
    
    def draw(self, vec):
        x = point[0]
        y = point[1]
        
        
        
root = tk.Tk()
Application.title = "Game"
app = Application(root)
app.mainloop()
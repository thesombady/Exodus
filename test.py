import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()

root.title("Exodus Game Engine")

root.geometry('900x400')
bitmap = Image.open('Exodus.jpg')
bitmap = ImageTk.PhotoImage(bitmap)
#canvas = tk.Canvas(root, width = 100, height = 100)
#canvas.pack()
label = tk.Label(image = bitmap)
label.pack()

root.mainloop()

import tkinter as tk
from PIL import Image, ImageTk

import numpy as np

class Bitmap:

    def __init__(self, size):
        self.width = size[0]
        self.height = size[1]

        self.bits = np.zeros((self.height, self.width, 3), np.uint8)
        self.w_pos = np.full((self.height, self.width), np.inf)

        self.xs = np.repeat(np.arange(self.width)[None, :], self.height, axis=0)
        self.ys = np.repeat(np.arange(self.height)[:, None], self.width, axis=1)

        self.scale = np.array([self.width / 2.0, self.height / 2.0, 1])
        self.offset = np.array([1, 1, 0])

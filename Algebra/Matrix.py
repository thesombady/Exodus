from Vector import vec2d
from math import sin, cos


class Matrix2d:

    def __init__(self, x1 = 1, x2 = 0, y1 = 0, y2 = 1):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.col1 = vec2d(self.x1, self.y1)
        self.col2 = vec2d(self.x2, self.y2)
        self.ma = (self.col1, self.col2)


    def __str__(self):
         return f'[({self.x1}, {self.x2})\n ({self.y1}, {self.y2})]'

    def __add__(self, other):
        return Matrix2d(self.x1 + other.x1, self.x2 + other.x2, self.y1 + other.y1, self.y2 + other.y2)

    def __sub__(self, other):
        return Matrix2d(self.x1 - other.x1, self.x2 - other.x2, self.y1 - other.y1, self.y2 - other.y2)

    def __getitem__(self, index):
        return self.ma[index]

    def __mul__(self, other):
        if isinstance(other, Matrix2d):
            nx1 = self.x1 * other.x1 + self.x2 * other.y1
            nx2 = self.x1 * other.x2 + self.x2 * other.y2
            ny1 = self.y1 * other.x1 + self.y2 * other.y1
            ny2 = self.y1 * other.x2 + self.y2 * other.y2
            return Matrix2d(nx1, nx2, ny1, ny2)
        else:
            return self.vecmul(other)

    def vecmul(self, vector):
        nx1 = self.x1 * vector[0] + self.x2 * vector[0]
        ny1 = self.y1 * vector[0] + self.y2 * vector[1]
        return vec2d(nx1, ny1)

    def rotation(self, theta):
        return Matrix2d(cos(theta), -sin(theta), sin(theta), cos(theta))

    def transpose(self):
        return Matrix2d(self.x1, self.y1, self.x2, self.y1)




class vec2d:
    """ Creates a vec2d object which represents a two dimensional vector in the standard R^2 plane. """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vector = (x,y)

    def __str__(self):
        return f'[({self.x},{self.y})]'

    def __add__(self, other):
        return vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        if isinstance(scalar, (float, int)):
            return vec2d(self.x * scalar, self.y * scalar)
        else:
            return self.cross(scalar)

    def __rmul__(self, scalar):
        return vec2d(self.x * scalar, self.y * scalar)

    def __getitem__(self, index):
        return self.vector[index]

    def dotproduct(self, other):
        scalar = self.x * other.x + self.y * other.y + self.y
        return scalar * scalar

    def norm(self):
        scalar = (self.x ** 2 + self.y ** 2) ** (0.5)
        return scalar

    def normalize(self):
        return 1/self.norm() * vec2d(self.x, self.y)

    def cross(self, other):
        return vec2d(self.x * other.y, other.x * self.y)

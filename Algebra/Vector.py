class vec3d:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = (self.x, self.y, self.z)

    def __str__(self):
        return f'([{self.x}, {self.y}, {self.z}])'

    def __add__(self, other):
        if isinstance(other, vec3d):
            return vec3d(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            pass

    def __sub__(self, other):
        if isinstance(other, vec3d):
            return vec3d(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            pass

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return vec3d(self.x * scalar, self.y * scalar, self.z * scalar)
        else:
            pass

    def __rmul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return vec3d(self.x * scalar, self.y * scalar, self.z * scalar)
        else:
            pass

    def __getitem__(self, index):
        return self.vector[index]

    def dot(self, other):
        if isinstance(other, vec3d):
            sum = self.x * other.x + self.y * other.y + self.z * other.z
            return sum
        else:
            pass

    def cross(self, other):
        if isinstance(other, vec3d):
            col1 = self.y * other.z - self.z * other.y
            col2 = self.z * other.x - self.x * other.z
            col3 = self.x * other.y - self.y * other.z
            return vec3d(col1, col2, col3)
        else:
            pass

    def norm(self):
        value = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1/2)
        return value

    def normalize(self):
        return 1 / self.norm() * self

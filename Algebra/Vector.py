


class vec2d(object):
    """ Creates a vec2d object which represents a two dimensional vector in the standard R^2 plane. """

    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def __str__(self):
        return f'[({self.x},{self.y})]'
    
    def __add__(self, other):
        return vec2d(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return vec2d(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return vec2d(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return vec2d(self.x * scalar, self.y * scalar)
    
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


class vec3d(object):
    """ Creates a vec3d object which represents a two dimensional vector in the standard R^3 plane. """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f'[({self.x},{self.y},{self.z})]'
    
    def __add__(self, other):
        return vec3d(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return vec3d(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        return vec3d(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __rmul__(self, scalar):
        return vec3d(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def dotproduct(self, other):
        scalar = self.x * other.x + self.y * other.y + self.y + self.z * other.z
        return scalar
    
    def norm(self):
        scalar = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (0.5)
        return scalar 
    
    def normalize(self):
        return 1/self.norm() * vec3d(self.x, self.y, self.z)



class vec2d(object):
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
        return vec2d(self.x * scalar, self.y * scalar)
    
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
    



class vec3d(object):
    """ Creates a vec3d object which represents a two dimensional vector in the standard R^3 plane. """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vector = (x,y,z)
    
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
    
    def __getitem__(self, index):
        return self.vector[index]
    
    def dotproduct(self, other):
        scalar = self.x * other.x + self.y * other.y + self.y + self.z * other.z
        return scalar
    
    def norm(self):
        scalar = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (0.5)
        return scalar 
    
    def normalize(self):
        return 1/self.norm() * vec3d(self.x, self.y, self.z)


class Matrix2d:

    def __init__(self, vec1, vec2):
        if not isinstance(vec1, (vec2d)):
            raise TypeError("Wrong input in matrix2d, not the vector input")
            
        self.vec1 = vec1 
        self.vec2 = vec2
    
    def __str__(self):
        return f'[({self.vec1[0]},{self.vec2[0]})\n ({self.vec1[1]},{self.vec2[1]})]'
    
    def __getitem__(self, index):
        if index == 0:
            return self.vec1
        elif index == 1:
            return self.vec2
    
    def trace(self):
        trace1 = self.vec1[0]
        trace2 = self.vec2[1]
        return trace1 + trace2
    
    def __add__(self, other):
        vec1 = self.vec1 + other[0] 
        vec2 = self.vec2 + other[1]
        return Matrix2d(vec1 ,vec2)
    
    def __mul__(self, other):
        ovec1 = other[0]
        ovec2 = other[1]
        pos1 = self.vec1[0] * ovec1[0] + self.vec1[1] * ovec1[0]
        pos2 = self.vec1[0] * ovec1[1] + self.vec1[1] * ovec1[1]
        pos3 = self.vec2[0] * ovec2[0] + self.vec2[1] * ovec2[0]
        pos4 = self.vec2[0] * ovec2[1] + self.vec2[1] * ovec2[1]
        vector1 = vec2d(pos1, pos2)
        vector2 = vec2d(pos3, pos4)
        return Matrix2d(vector1, vector2)

    def vecmul(self, vector):
        element1 = self.vec1[0] * vector[0] + self.vec2[0] * vector[1]
        element2 = self.vec1[1] * vector[0] + self.vec2[1] * vector[1]
        return vec2d(element1, element2)

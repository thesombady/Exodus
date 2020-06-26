from Vector import vec3d

class matrix3d:
    Standard = {
        "Unit" : (vec3d(1,0,0), vec3d(0,1,0), vec3d(0,0,1))
    }

    def __init__(self, vec1, vec2, vec3):
        self.vec1 = vec1
        self.vec2 = vec2
        self.vec3 = vec3
        self.matrix = (self.vec1, self.vec2, self.vec3)

    def __getitem__(self, index):
        if len(index) == 2:
            col = self.matrix[index[0]]
            return col[index[1]]
        elif len(index) == 1 or isinstance(index, (int)):
            return self.matrix[index]
        else:
            pass

    def __str__(self):
        return f'[{self.vec1}\n {self.vec2}\n {self.vec3}]'

    def __add__(self, other):
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 + other.vec1, self.vec2 + other.vec2, self.vec3 + other.vec3)
        else:
            pass

    def __sub__(self, other):
        if isinstance(other, matrix3d):
            return matrix3d(self.vec1 - other.vec1, self.vec2 - other.vec2, self.vec3 - other.vec3)
        else:
            pass

    def __mul__(self, other):
        if isinstance(other, matrix3d):#Matrix multiplication
            x1 = self.vec1[0] * other.vec1[0] + self.vec1[1] * other.vec2[0] + self.vec1[2] * other.vec3[0]
            y1 = self.vec1[0] * other.vec1[1] + self.vec1[1] * other.vec2[1] + self.vec1[2] * other.vec3[1]
            z1 = self.vec1[0] * other.vec1[2] + self.vec1[1] * other.vec2[2] + self.vec1[2] * other.vec3[2]

            x2 = self.vec2[0] * other.vec1[0] + self.vec2[1] * other.vec2[0] + self.vec2[2] * other.vec3[0]
            y2 = self.vec2[1] * other.vec2[1] + self.vec2[1] * other.vec2[1] + self.vec2[2] * other.vec3[1]
            z2 = self.vec2[1] * other.vec2[2] + self.vec2[1] * other.vec2[2] + self.vec2[2] * other.vec3[2]

            x3 = self.vec3[0] * other.vec1[0] + self.vec3[1] * other.vec2[0] + self.vec3[2] * other.vec3[0]
            y3 = self.vec3[0] * other.vec1[1] + self.vec3[1] * other.vec2[1] + self.vec3[2] * other.vec3[1]
            z3 = self.vec3[0] * other.vec1[2] + self.vec3[1] * other.vec2[2] + self.vec3[2] * other.vec3[2]

            vec1, vec2, vec3 = vec3d(x1, y1, z1), vec3d(x2, y2, z2), vec3d(x3, y3, z3)
            return matrix3d(vec1, vec2, vec3)
        elif isinstance(other, (int, float)):#Scalar multiplication
            return matrix3d(self.vec1 * other, self.vec2 * other, self.vec3 * other)
        elif isinstance(other, vec3d): #Vector Transformation
            x = self.vec1[0] * other[0] + self.vec1[1] * other[1] + self.vec1[2] * other[2]
            y = self.vec2[0] * other[0] + self.vec2[1] * other[1] + self.vec2[2] * other[2]
            z = self.vec3[0] * other[0] + self.vec3[1] * other[1] + self.vec3[2] * other[2]
            return vec3d(x, y, z)

    def trace(self):
        return self.vec1[0] + self.vec2[1] + self.vec3[2]

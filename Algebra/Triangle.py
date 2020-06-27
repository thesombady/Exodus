from Vector import vec3d

class triangle3d:

    def __init__(self, vec1, vec2, vec3):
        self.vec1 = vec1
        self.vec2 = vec2
        self.vec3 = vec3


class Mesh:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f'{self.args}'

vec1=vec3d(1,0,0)
vec2=vec3d(0,1,0)
vec3=vec3d(0,0,1)
tris = triangle3d(vec1, vec2, vec3)
mesh = Mesh(tris)
print(mesh[0])

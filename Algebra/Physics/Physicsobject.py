import matplotlib.pyplot as plt

class PhysicalObject:

    def __init__(self, x1 = 0, x2 = 0, y1 = 0, y2 = 0, solid = True):
        if solid == False:
            raise KeyError("[System:] If you want a non-solid object, dont use PhyscalObject class")
        self.solid = solid
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.width = abs(x2 - x1)
        self.height = abs(y2 - y1)

    def __str__(self):
        return f'{self.width}, {self.height}, {self.solid}'

    def __repr__(self):
        return f'{self.x2}, {self.y2}, {self.solid}'




#object1 = PhysicalObject(x2 = 10, y2 = 10)
#print(object1)

class Object(PhysicalObject):

    objects = {
    "Box" : "Something",
    "Circle" : "Something"
    }

    def __init__(self, x1 = 0, x2 = 0, y1 = 0, y2 = 0, solid = True, objecttype = "Box"):
        super().__init__(x1, x2, y1, y2, solid)
        if objecttype == "Box" or objecttype == "Circle":
            self.objecttype = objecttype
        else:
            raise KeyError("That object do not exist.")

    def intalize(self):
        if self.objecttype == "Box":
            self.drawbox()
        elif self.objecttype == "Circle":
            self.drawcircle()

    def drawbox(self):
        pass

    def drawcircle(self):
        pass







object1 = Object(x2 = 10, y2 = 10)

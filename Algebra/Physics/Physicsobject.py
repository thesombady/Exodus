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
        self.vector = (self.x1, self.y1, self.x2, self.y2)

    def __str__(self):
        return f'X1={self.x1}, Y1={self.y1}, X2 = {self.x2}, Y2={self.y2}, Solid={self.solid}'

    def __repr__(self):
        return f'X1={self.x1}, Y1={self.y1}, X2 = {self.x2}, Y2={self.y2}, Solid={self.solid}'

    def __getitem__(self, index):
        return self.vector[index]




#object1 = PhysicalObject(x2 = 10, y2 = 10)
#print(object1)

class Object(PhysicalObject):

    objects = {
    "Box" : "Something",
    "Circle" : "Something"
    }

    Ingame_objects = {}

    def __init__(self, x1 = 0, x2 = 0, y1 = 0, y2 = 0, solid = True, objecttype = "Box", name = None):
        super().__init__(x1, x2, y1, y2, solid)
        if objecttype == "Box" or objecttype == "Circle":
            self.objecttype = objecttype
        else:
            raise KeyError("That object do not exist.")
        self.name = name
        self.addobjects()


    def addobjects(self):
        self.Ingame_objects[self.name] = (self.x1, self.y1, self.x2, self.y2)
        print(self.Ingame_objects)

    def intalize(self):
        if self.objecttype == "Box":
            self.drawbox()
        elif self.objecttype == "Circle":
            self.drawcircle()

    def drawbox(self):
        pass

    def drawcircle(self):
        pass

    def addvec(self, vector2):
        usefullobjects = []
        for key in self.Ingame_objects:
            if key != self.name:
                usefullobjects.append(self.Ingame_objects[key]) # position = (x1, y1, x2, y2)
        possibilites = []
        for object in usefullobjects:
            if (object[0] - vector2[0])>0:
                possibilites.append(True)
            else:
                possibilites.append(False)

        if not False in possibilites:
            print('[System:] Could move')
        else:
            print('[System:] Could not move')



object1 = Object(x1 = 8, x2 = 11,y1=1, y2 = 1, name = 'object1')
player = Object(name = 'player')
player.addvec((1,0))

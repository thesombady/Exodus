import time

class Physicalobject:

    def __init__(self, x1 = 0, x2 = 0, y1 = 0, y2 = 0, solid = True):
        self.solid = solid
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class object(Physicalobject):

    objects = {}

    def __init__(self, x1, x2, y1, y2, solid = True, name = ''):
        super().__init__(x1, x2, y1, y2, solid)
        if self.solid == True:
            self.width = self.x2 - self.x1
            self.height = self.y2 - self.y1
            self.name = name
            self.intialize()

    def intialize(self):
        self.objects[self.name] = (self.x1, self.x2, self.y1, self.y2)
        print(self.objects)

    def nearestobject(self):
        allobjects = []
        for key in self.objects:
            if not key == self.name:
                allobjects.append(self.objects[key])
        for i in range(allobjects):
            pass



class simplehysicalobject:
    def __init__(self, x = 0, y = 0, solid = True):
        self.x = x
        self.y = y
        self.solid = solid
class simpleobjects(simplehysicalobject):
    objects = {}

    def __init__(self, x = 0, y = 0, solid = True, name = ''):
        super().__init__(x, y, solid)
        self.name = name
        if self.solid == True:
            self.objects[self.name] = (self.x, self.y)

    def nearestobject(self):
        all_objects = []
        for key in self.objects:
            if key != self.name:
                all_objects.append(self.objects[key])
        print(all_objects)
        xcorobjects = []
        ycorobjects = []
        for i in range(len(all_objects)):
            xcorobjects.append(all_objects[i][0])
            ycorobjects.append(all_objects[i][1])
        print(xcorobjects, ycorobjects)
        xcorobjects = [self.x - i for i in xcorobjects]
        ycorobjects = [self.y - i for i in ycorobjects]
        nearestobject =(min(xcorobjects), min(ycorobjects))
        print(nearestobject)






player = simpleobjects(1,0, name = 'hello')
object1 = simpleobjects(0,0, name = 'box1')
object2 = simpleobjects(1,1, name = 'box2')
player.nearestobject()

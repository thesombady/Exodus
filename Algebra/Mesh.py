from Vector import vec2d

class mesh:

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.initialize()

    def initialize(self):
        self.xaxis = []
        self.yaxis = []
        for i in range(self.x1, self.x2 +1):
            self.xaxis.append(i)
            yaxis = []
            for j in range(self.y1, self.y2 +1):
                yaxis.append(j)
            self.yaxis.append(yaxis)
        #print(self.xaxis, self.yaxis)
        return self.xaxis, self.yaxis

    def draw(self):
        pass




#mesh1 = mesh(0, 2, 0, 2)

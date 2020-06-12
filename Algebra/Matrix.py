

class matrix2d(object):
    """ This creates a matrix2d object which represent the matrix of a twodimensional vector set. """

    def __init__(self, values):
        self.values = values
    
    def __str__(self):
        return f'[({self.values[0]}, {self.values[1]})\n ({self.values[2]}, {self.values[3]})]'


    def __add__(self, other):
        #values = (self.values[0] + other[0], self.values[1] + other[1], self.values[2] + other[2], self.values[3] +  other[3])
        value0 = self.values[0] + other[0]
        value1 = self.values[1] + other[1]
        value2 = self.values[2] + other[2]
        value3 = self.values[3] + other[3]
        values = (value0, value1, value2, value3)
        return matrix2d(values)

unit = (1,0,0,1)
revunit=(-1,0,0,-1)
    
matrix = matrix2d(unit)
rematrix = matrix2d(revunit)
print(rematrix + matrix)
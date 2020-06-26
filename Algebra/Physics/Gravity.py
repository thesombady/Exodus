class Gravity:
    GConstant = 9.81

    def __init__(self):
        pass

    def Pull(self, mass):
        return mass * self.GConstant

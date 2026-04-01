from multimethod import multimethod
import math

class MiPunto:

    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    @multimethod
    def distancia(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    @multimethod
    def distancia(self, x: float, y: float):
        return math.sqrt((self.x - x)**2 + (self.y - y)**2)


p1 = MiPunto()
p2 = MiPunto(10, 30.5)

print(p1.distancia(p2))      
print(p1.distancia(10.0, 30.5)) 
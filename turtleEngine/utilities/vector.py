import math

class Vector:
    def __init__(self):
        pass

    @classmethod
    def v2(cls, x:float, y:float):
        myClass = cls()
        myClass.x = x
        myClass.y = y
        myClass.z = 0
        return myClass

    @classmethod
    def v3(cls, x:float, y:float, z:float):
        myClass = cls()
        myClass.x = x
        myClass.y = y
        myClass.z = z
        return myClass
    
    def norme(self):
        return (math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2)))
    
    @staticmethod
    def distance(vec1,vec2):
        x = abs(vec1.x - vec2.x)
        y = abs(vec1.y - vec2.y)
        z = abs(vec1.z - vec2.z)

        return Vector.norme(Vector.v3(x,y,z))
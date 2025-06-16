from ..utilities.vector import Vector


class Face:
    def __init__(self, vertex:list, color:str, averagePosition=False):
        self.vertex = vertex
        self.color = color


        mX = 0
        mY = 0
        mZ = 0

        for v in vertex:
            mX += v.x
            mY += v.y
            mZ += v.z
        
        self.averagePosition = averagePosition
        if not averagePosition:
            self.averagePosition = Vector.v3(mX//len(vertex), mY//len(vertex), mZ//len(vertex))

    def setDistance(self,d):
        self.distance = d

    @staticmethod
    def distanceKey(obj):
        return obj.distance
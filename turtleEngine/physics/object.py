from ..utilities.vector import Vector
from ..rendering.face import Face

class Object:
    def __init__(self, vertexList, facesList:list=[]):
        self.vertex = vertexList
        self.faces = facesList

import turtle
from ..utilities.vector import Vector
from .face import Face
from ..physics.object import Object

class Camera:
    def __init__(self,  focalLenght:int, position:Vector.v3=Vector.v3(0,0,0)):
        self.position = position
        self.focalLenght = focalLenght
        
        self.screen = turtle.Screen()
        self.screen.tracer(0)

        self.pen = turtle.Turtle()
        self.pen.up()
        self.pen.color('black')
        self.pen.pensize(5)
        self.pen.hideturtle()

        self.vertex = []
        self.links = []

    def vertexProjector(self, vertex=[], link=[]):
        self.vertex = []
        self.links = []

        for v in vertex:
            x = v.x * (self.focalLenght / abs(v.z - self.position.z))
            y = v.y * (self.focalLenght / abs(v.z - self.position.z))
            self.vertex.append(Vector.v2(x, y))

        for v in link:
            x = v.x * (self.focalLenght / abs(v.z - self.position.z))
            y = v.y * (self.focalLenght / abs(v.z - self.position.z))
            self.links.append(Vector.v2(x, y))

    def faceProjector(self, faces):
        self.faces = []

        for face in faces:
            fVertex = []
            posBuffer = face.averagePosition
            for v in face.vertex:
                x = v.x * (self.focalLenght / abs(v.z - self.position.z))
                y = v.y * (self.focalLenght / abs(v.z - self.position.z))
                fVertex.append(Vector.v2(x,y))
            self.faces.append(Face(fVertex, face.color, posBuffer))
                
        for face in self.faces:
            face.setDistance(Vector.distance(face.averagePosition, self.position))

        self.faces = sorted(self.faces, key=Face.distanceKey, reverse=True)

    def wireframeShader(self):
        self.pen.color('black')
        self.pen.pensize(5)
        self.pen.clear()
        for v in self.vertex:
            self.pen.goto(v.x, v.y)
            self.pen.dot(5)
        
        for v in range (0, len(self.links), 2):
            self.pen.goto(self.links[v].x, self.links[v].y)
            self.pen.down()
            self.pen.goto(self.links[v+1].x, self.links[v+1].y)
            self.pen.up()

    def faceShader(self, blackEdges=False):
        self.pen.clear()

        for face in self.faces:
            self.pen.goto(face.vertex[0].x, face.vertex[0].y)
            if blackEdges:
                self.pen.color('black', face.color)
                self.pen.pensize(10)
            else:
                self.pen.color(face.color)
                self.pen.pensize(1)
            
            self.pen.begin_fill()
            
            for v in face.vertex:
                self.pen.goto(v.x, v.y)
                self.pen.down()

            self.pen.end_fill()
            self.pen.up()                

    def renderObject(self, obj:Object, blackEdges=False):
        self.faceProjector(obj.faces)
        self.faceShader(blackEdges)

    def update(self):
        self.screen.update()
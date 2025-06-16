from turtleEngine import *
from time import sleep
from math import pi, cos, sin

focalLenght = 1000
rotation = pi/700
sleepTime = 0.01

cam = Camera(focalLenght)
cam.position.z = -50

A = Vector.v3(-5,5,-5)
B = Vector.v3(5,5,-5)
C = Vector.v3(5,5,5)
D = Vector.v3(-5,5,5)

E = Vector.v3(-5,-5,-5)
F = Vector.v3(5,-5,-5)
G = Vector.v3(5,-5,5)
H = Vector.v3(-5,-5,5)

vertex = [A,B,C,D,E,F,G,H]

links = [
    A,B,
    B,C,
    C,D,
    D,A,

    E,F,
    F,G,
    G,H,
    H,E,

    A,E,
    B,F,
    C,G,
    D,H
]

def rotateCubeY(angle):
    # around y
    for v in vertex:
        v.x = cos(angle) * v.x + sin(angle) * v.z
        v.z =-sin(angle) * v.x + cos(angle) * v.z

def rotateCubeX(angle):
    # around x
    for v in vertex:
        v.y = cos(angle) * v.y - sin(angle) * v.z
        v.z = sin(angle) * v.y + cos(angle) * v.z
    

while True:
    # vertex test
    if 0:
        sleep(sleepTime)

        rotateCubeY()

        cam.vertexProjector(link=links)
        cam.wireframeShader()
        cam.update()

    # face test
    if 1:
        sleep(sleepTime)

        rotateCubeY(rotation)
        rotateCubeX(rotation)

        faces = [
            Face([A,B,C,D],"blue"),
            Face([E,F,G,H],"red"),
            Face([A,B,F,E],"green"),
            Face([B,F,G,C],"purple"),
            Face([C,G,H,D],"orange"),
            Face([D,H,E,A],"yellow"),

        ]

        cam.faceProjector(faces)
        cam.faceShader(blackEdges=False)
        cam.update()



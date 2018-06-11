# Mover

# Using PVector class
from PVector import PVector

class Mover:
    def __init__(self, massValue=None, x=None, y=None):
        if x != None and y != None:
            self.p = PVector(x, y)
        else:
            self.p = PVector(width / 2, height / 2)
        self.v = PVector(0, 0)
        self.a = PVector(0, 0)
        self.r = random(255)
        
        if massValue != None:
            self.mass = massValue


    def applyForce(self, force=PVector(0, 0)):
        f = PVector().div(force, self.mass)
        self.a.add(f)

    def update(self):
        self.v.add(self.a)
        self.p.add(self.v)
        self.a.mult(0)

    def display(self):
        stroke(0)
        fill(self.r)
        ellipse(self.p.x, self.p.y, 20, 20)

    def checkEdges(self):
        if self.p.x > width:
            self.v.x *= -1
            #self.p.x = 0
        elif self.p.x < 0:
            #self.p.x = width
            self.v.x *= -1

        if self.p.y > height:
            self.v.y *= -1
            self.p.y = height

        elif self.p.y < 0:
            self.v.y *= -1


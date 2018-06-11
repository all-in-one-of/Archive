
# Using PVector class
from PVector import PVector

class Mover:
    def __init__(self):
        self.p = PVector(random(width), random(height))
        self.v = PVector(0,0)
        self.a = PVector(-0.001,0.01)
        self.r = random(255)
        
    def update(self):
        
        magnitude = 0.3
        m = PVector(mouseX, mouseY)
        dir = PVector().sub(m, self.p)
        
        dir.normalize()
        dir.mult(magnitude)
        
        self.a = dir
        self.v.add(self.a)
        self.p.add(self.v)
        self.v.limit(5)
        
    def display(self):
        stroke(0)
        fill(self.r)
        ellipse(self.p.x, self.p.y, 20, 20)
        
    def checkEdges(self):
        jitter = (width+height)/2
        if self.p.x > width:
            self.p.x = 0
            self.p.y += random(jitter)
        elif self.p.x < 0:
            self.p.x = width
            self.p.y += random(jitter)
        
        if self.p.y > height:
            self.p.y = 0
            self.p.x = random(jitter)
        elif self.p.y < 0:
            self.p.y = height
            self.p.x = random(jitter)
            

movers = []

def setup():
    size(600, 600)
    background(255)
    movers = [Mover() for i in range(0,10)]

def draw():
    background(255)
    for m in movers:
        m.update()
        m.checkEdges()
        m.display()
    




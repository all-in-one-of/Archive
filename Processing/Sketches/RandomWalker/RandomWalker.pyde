
# Nature of Code - Introduction
# http://natureofcode.com/book/introduction/

class Walker:
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.x = w
        self.y = h
    def display(self):
        stroke(0);
        point(self.x, self.y)
    def step(self):
        stepmax = 2
        stepmin = -stepmax
        
        stepx = float(random(stepmin, stepmax))
        stepy = float(random(stepmin, stepmax))
        
        self.x += stepx
        self.y += stepy
        
    def levystep(self, probability, largestep):
        
        r = float(random(1))
        if r < probability:
            stepmax = largestep
        else:
            stepmax = 2
        
        stepmin = -stepmax
        stepx = float(random(stepmin, stepmax))
        stepy = float(random(stepmin, stepmax))
        
        self.x += stepx
        self.y += stepy


w = None

def setup():
    size(640, 360)
    w = Walker(width/2, height/2)
    background(255)

def draw():
    #w.step()
    w.levystep(0.1,20)
    w.display()





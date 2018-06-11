
# Forces
from Mover import Mover

maxCount = 20
movers = []
gravities = []
winds = []


def setup():
    size(600, 600)
    background(255)
    movers = [Mover(random(1, 1000), width/2, height/2) for i in range(0,maxCount)]
    gravities = [PVector(0, 0.1 * movers[i].mass) for i in range(0, maxCount)]
    winds = [PVector(random(-10,10), 0) for i in range(0, maxCount)]

def draw():
    background(255)
    for i in range(0, maxCount):
        m = movers[i]
        gravity = gravities[i]
        wind = winds[i]
        
        m.applyForce(wind)
        m.applyForce(gravity)
        
        m.update()
        
        m.display()
        m.checkEdges()

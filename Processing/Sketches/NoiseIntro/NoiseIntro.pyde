
class Walker:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tx = 0
        self.ty = 10000
    def step(self, w, h):
        self.x = map(noise(self.tx), 0, 1, 0, w)
        self.y = map(noise(self.ty), 0, 1, 0, h)
        
        self.tx += 0.01
        self.ty += 0.01
        
        ellipse(self.x, self.y, 16, 16)

w = None

def setup():
    size(600,600)
    background(255)
    w = Walker()

def draw():
    w.step(width, height)



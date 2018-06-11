
# PVector

class PVector:
    def __init__(self, x1 = None, y1 = None):
        if x1 != None:
            self.x = x1
        if y1 != None:
            self.y = y1
    
    def add(self, v, w = None):
        if w == None:
            self.x += v.x
            self.y += v.y
        else:
            return PVector(v.x + w.x, v.y + w.y)
        
    def sub(self, v, w = None):
        if w == None:
            self.x -= v.x
            self.y -= v.y
        else:
            return PVector(v.x - w.x, v.y - w.y)
    
    def mult(self, n):
        self.x *= n
        self.y *= n
        
    def div(self, a = None, n = None):
        if a != None and n != None:
            return PVector(a.x/n, a.y/n)
        else:
            self.x /= n
            self.y /= n
    
    def mag(self):
        return sqrt(self.x * self.x + self.y * self.y)
    
    def normalize(self):
        m = self.mag()
        if m != 0:
            self.div(m)
            
    def limit(self, value):
        if self.mag() > value:
            self.normalize()
            self.mult(value)
            
        
if __name__ == "__main__":
    p = PVector()



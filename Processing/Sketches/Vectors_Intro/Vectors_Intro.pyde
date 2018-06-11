
# Bouncing ball with No Vectors

x = 100
y = 100
xspeed = random(5)
yspeed = random(5)

def setup():
    size(640, 360)
    background(255)
    x = width/2
    y = height/2

def draw():
    x += xspeed
    y += yspeed
    
    if x > width or x < 0:
        xspeed = (-1) * xspeed
        
    if y > height or y < 0:
        yspeed = (-1) * yspeed
    
    background(255)
    stroke(1)
    fill(200)
    
    ellipse(x,y, 15, 15)

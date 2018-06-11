
divs = 50
segments = 1

def setup():
    size(500, 500)
    background(255)

def draw():
    background(255)

    stroke(200)
    segments = width / divs
    for x in range(1, divs):
        line(x * segments, 0, x * segments, height)

    segments = height / divs
    for y in range(1, divs):
        line(0, y * segments, width, y * segments)

    stroke(0, 0, 200)
    line(0, height, mouseX, mouseY)
    
    segments = width / divs
    x = abs(mouseX * divs/width) * segments
    stroke(200, 0, 0)
    line(0, mouseY, x, mouseY)
    
    segments = height / divs
    y = (abs(mouseY * divs/height)+1) * segments
    stroke(0, 200, 0)
    line(mouseX, height, mouseX, y)
    


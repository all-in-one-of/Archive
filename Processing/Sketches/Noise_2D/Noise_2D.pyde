
# Nature of Code
# 2D Perlin Noise

x = 0
y = 0
xoff = 0.0
yoff = 0.0

size(600,600)
loadPixels()

for x in range(0, width):
    yoff = 0.0
    for y in range(0, height):
        bright = float(map(noise(xoff, yoff), 0, 1, 0, 255))
        pixels[x+y * width] = color(bright)
        yoff += 0.01
    xoff += 0.01
        
updatePixels()

    

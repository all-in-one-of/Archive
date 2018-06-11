
# Nature of Code - Introduction
# http://natureofcode.com/book/introduction/

maxCount = 30

randomCounts = [0 for i in range(0, maxCount)]

def setup():
    size(600,300)
    background(255)
    
def draw():
    i = int(random(len(randomCounts)))
    randomCounts[i] += 1
    
    stroke(0)
    fill(175)
    w = width/len(randomCounts)
    
    for j in range(0, len(randomCounts)):
        rect(j*w, height - randomCounts[j], w-1, randomCounts[j])

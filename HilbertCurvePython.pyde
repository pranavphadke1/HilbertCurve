order = 1
N = pow(2,order)
total = int(N*N)

path = []

def setup():
    size(700,700)
    colorMode(HSB, 360, 255, 255)
    background(0)
    
    for i in range (total):
        # print(i)
        path.append(hilbert(i))
        len = width / N
        path[i].mult(len)
        path[i].add(len/2,len/2,0)
    
    
    
def hilbert(i):
    points = [PVector(0,0), PVector(0,1), PVector(1,1), PVector(1,0)]
    
    
    #BitMasking to get the points of an order 1 PHC
    index = i & 3; 
    v = points[index];    

    for j in range (1, order):
        #Now BitShift to get the quadrant of the PHC
        
        i = i >> 2
        index = i & 3
        
        #need to shift positionby order value ?? (17 min)
        len = pow(2,j)
        if (index == 0):
            #in quad1
            temp = v.x
            v.x = v.y
            v.y = temp
        elif (index == 1):
            #in quad 2
            v.y += len
        elif (index == 2):
            # in quad 3
            v.x += len
            v.y += len
        elif (index == 3):
            #in quad 4
            #?????
            temp = len - 1 - v.x
            v.x = len - 1 - v.y 
            v.y = temp
            v.x += len    
    return v

counter = 0
def draw():
    global counter
    background(0)
    #Sets the color used to draw lines and borders around shapes
    stroke(255)
    strokeWeight(2)
    noFill()
    #beginShape()
    # for i in range (1, counter):
    for i in range (1, len(path)):
        h = map(i,0,len(path),0,360)
        stroke(h,255,255)
        line(path[i].x, path[i].y, path[i-1].x, path[i-1].y)
    #endShape()
    #essentially changes the speed of animation
    counter += 50
    if (counter > len(path)):
        counter = 0
    # saveFrame("orders/hilbert_8.png")

order = 1
N = pow(2,order)
total = int(N*N)

# Represents the 1 dimensional curve consisting of points mapping to a 2 dimensional plane.
path = []

def setup():
    # Can be changed to resize animation box.
    size(1024,1024)
    # Adds a transition of color to help visually understand that the pattern is in face one curve.
    colorMode(HSB, 360, 255, 255)
    background(0)
    
    for i in range (total):
        path.append(hilbert(i))
        len = width / N
        path[i].mult(len)
        path[i].add(len/2,len/2,0)
    
    
# Given an index (from list "path"), outputs the (x,y) location of where that index is in an order 1 psuedo hilbert curve.
def hilbert(i):
    # This is the order of points in an order 1 psuedo hilbert curve (PHC).
    points = [PVector(0,0), PVector(0,1), PVector(1,1), PVector(1,0)]
    
    
    # BitMasking to get the index corresponding to (x,y) point from list "points." 
    # Looks at the binary representation of the integer "index" and applys logical AND to each bit with the binary representation of 3.
    # Result is a 00...00XY where XY can each be either a 1 or a 0 depending on the AND result of those bits with the last two bits of binary 3 (11).
    index = i & 3; 
    # Gets the specific (x,y) location of of an order 1 PHC based on the "index" value.
    v = points[index];    

    # Loops through all the order values to create the connection of a bunch of order 1 PHCs to create an order "order" hilbert curve.
    for j in range (1, order):
        # Now BitShift to get the quadrant of the PHC.
        # Essentially drop the last two bits of the binary representation of i.
        # Assign i to be the conversion of that new binary number into its decimal representation.
        i = i >> 2
        # Another BitMasking tells us which quadrant we are in
        quadrant = i & 3
        
        # Need to shift position by 2^order value. 
        # This is because an order 1 PHC of an order 2 PHC should be 2^2 away from an order 1 PHC that is contain inside another order 2 PHC.
        # Ensures that each PHC order variation doesn't stack upon each other. 
        len = pow(2,j)
        if (quadrant == 0):
            #in quad1
            temp = v.x
            v.x = v.y
            v.y = temp
        elif (quadrant == 1):
            #in quad 2
            v.y += len
        elif (quadrant == 2):
            # in quad 3
            v.x += len
            v.y += len
        elif (quadrant == 3):
            #in quad 4
            #?????
            temp = len - 1 - v.x
            v.x = len - 1 - v.y 
            v.y = temp
            v.x += len    
    return v

counter = 0
def draw():
    # Must declare counter as a global as the draw function is continuously called. 
    # For animation to reset, counter must be tracked outside the function.
    global counter
    background(0)
    #Sets the color used to draw lines and borders around shapes
    stroke(255)
    strokeWeight(2)
    noFill()
    # Below loop is used for the animation representation.
    # for i in range (1, counter):
    # This loop instantly creates the still image representation.
    for i in range (1, len(path)):
        h = map(i,0,len(path),0,360)
        stroke(h,255,255)
        line(path[i].x, path[i].y, path[i-1].x, path[i-1].y)
    # Essentially changes the speed of animation.
    # Only used during animation representation.
    counter += 10
    # Resets the animation once complete
    if (counter > len(path)):
        counter = 0
        
    # Below is used to save images of the hilbert curve 
    # saveFrame("orders/hilbert.png")

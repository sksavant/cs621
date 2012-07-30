# Copyright (C) 2012 Savant Krishna
# 
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by Free Software 
# Foundation; either version 3 or (at your option) higher
# 
# This program tries to solve the knight's tour problem
# 
# Problem Statement: 
# In a chessboard of size 8X8 , given a position of a knight, find a tour 
# which will go to each of the squares exactly once.
# 
# Implementation:
# There are known solutions for the knight's tour using 
# *Divide and Conquer algorithms
# *Neural Networks :
# *Heurestic methods : Warnsdorff's rule
# 
# This program implements the Divide and Conquer algorithm to find knight's tour
#
#Initialising the chess board with the number of moves possible from each position

def validxy(x,y,n):
    if 0<=x<n and 0<=y<n:
        return True
    return False

gotn=0
notgotn=0
notgotpos=[]
gotpos=[]

def findknightstour(inp,n):
    global gotn
    global notgotn
    global gotpos
    global notgotpos
    ind=0
    index=[[-1 for i in range(n)] for i in range(n)]
    board=[
    [2,3,4,4,4,4,3,2],
    [3,4,6,6,6,6,4,3],
    [4,6,8,8,8,8,6,4],
    [4,6,8,8,8,8,6,4],
    [4,6,8,8,8,8,6,4],
    [4,6,8,8,8,8,6,4],
    [3,4,6,6,6,6,4,3],
    [2,3,4,4,4,4,3,2],
    ]
    touched=[[0 for i in range(n)] for j in range(n)]
    start=[int(inp[0]),int(inp[1])]
    end=[]
    xchanges=[1,2,-1,-2]
    ychanges=[1,2,-1,-2]
    #change x and y such that not go out of bounds and abs(xchanges[i])!=abs(ychanges[i])
    foundtour=False
    currentpos=start
    tour=[currentpos]
    index[currentpos[0]][currentpos[1]]=ind
    while not foundtour:
        touched[currentpos[0]][currentpos[1]]=1
        minaccess=1000
        touchedsth=False
        for xi in xchanges:
            xnew=currentpos[0]+xi
            for yi in ychanges:
                if not abs(xi)==abs(yi):
                    ynew=currentpos[1]+yi
                    if validxy(xnew,ynew,n):
                        if(not touched[xnew][ynew]):
                            if board[xnew][ynew]<minaccess:
                                minaccess=board[xnew][ynew]
                                nextpos=[xnew,ynew]
                                touchedsth=True
                            board[xnew][ynew]=board[xnew][ynew]-1
        if touchedsth:
            ind=ind+1
            currentpos=nextpos
            tour.append(currentpos)
            index[currentpos[0]][currentpos[1]]=ind
        else:
            anytouchedleft=False
            for e in touched:
                for f in e:
                    if not f:
                        print "Got into deadend\nThe board is :"
                        anytouchedleft=True
                        notgotn=notgotn+1
                        notgotpos.append(start)
                        findknightstour(str(start[0])+str(start[1]),n)
            if not anytouchedleft:
                foundtour=True
                for indexa in index:
                    print indexa
                print len(tour)
                gotn=gotn+1
                gotpos.append(start)

for i in range(8):
    for j in range(8):
        findknightstour(str(i)+str(j),8)

#findknightstour("13",8)
print gotn
print notgotn
print notgotpos
if False:
    testing=False+True
    alptoint={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
    chessboard=[[0 for i in range(8)] for j in range(8)]
    moves=[
    [2,3,4,4,4,4,3,2],
    [3,4,6,6,6,6,4,3],
    [4,6,8,8,8,8,6,4],
    [4,6,8,8,8,8,6,4],
    [4,6,8,8,8,8,6,4],
    [4,6,8,8,8,8,6,4],
    [3,4,6,6,6,6,4,3],
    [2,3,4,4,4,4,3,2],
    ]
    if testing :
        for e in chessboard:
            print e
    #Take the input for the initial knight's position
    inp=raw_input()
    assert(len(inp)==2)
    assert(str(inp[0]).lower() in ["a","b","c","d","e","f","g","h"])
    assert(int(inp[1]) in [i+1 for i in range(8)])
    s=[alptoint[inp[0].lower()],int(x[1])]
    if testing:
        print s
    e=[]
    foundtour=False
    while not foundtour:
        x=1
    #checking if tour is found and setting foundtour=True


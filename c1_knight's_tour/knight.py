# Problem Statement:
# In a chessboard of size 8X8 , given a position of a knight, find a closed tour
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

tours=[]
boardSize=int(raw_input("Size of the board : "))
knight=(0,0)
moves=[]
board=[["" for i in range(boardSize)] for i in range(boardSize)]
visited=0


def findclosedtour():
    #find a brute force tour starting from (0,0)
    #check if it is closed
    #if not find another random tour
    #Any algo optimised to find closed tours?
    global knight, board,visited,moves

    visited+=1
    board[knight[0]][knight[1]]=str(visited)
    moves.append([knight])
    #Starts out at starting position
    #how to find a brute force tour?
    #Start with (0,0)
    possiblemoves=validmoves(knight)
    for movei in possiblemoves:
        moves[0].append(movei)
    notfoundclosed=True
    while notfoundclosed:
        currentpos=len(moves)-1
        if(len(moves[currentpos]))>1:
            knight=findthebestmove(currentpos)
            visited+=1
            board[knight[0]][knight[1]]=str(visited)
            moves.append([knight])
            possiblemoves=validmoves(knight)
            for movei in possiblemoves:
                moves[currentpos+1].append(movei)
        else:
            if len(moves) >=boardSize**2:
                firstmove=moves[0][0]
                lastmove=moves[-1][0]
                if(abs(firstmove[0]-lastmove[0])==2 and abs(firstmove[1]-lastmove[1])==1) or (abs(firstmove[0]-lastmove[0])==1 and abs(firstmove[1]-lastmove[1])==2):
                    tours.append([i[0] for i in moves])
                    print "The closed tour is"
                    print tours[-1]
                    print "The board is"
                    for e in board:
                        print e
                    array=[]
                    strin=""
                    for e in tours[-1]:
                        array.append(str(8*int(e[0])+int(e[1])))
                        strin=strin+str(8*int(e[0])+int(e[1]))+ " \ "
                    notfoundclosed=False
                    print "The output is"
                    print strin
                    print array
                    return
                else:
                    gobacktoprev(knight)
            else:
                gobacktoprev(knight) #going back to prev squaure
    return


def validxy(x,y,n):
    if 0<=x<n and 0<=y<n:
        return True
    return False

def validmoves((y,x)):
    global boardSize,board
    listtoret=[]
    xychanges=[1,2,-1,-2]
    for xi in xychanges:
        xnew=xi+x
        for yi in xychanges:
            if not abs(xi)==abs(yi):
                ynew=yi+y
                if validxy(ynew,xnew,boardSize):
                    if board[ynew][xnew]=="":
                        listtoret.append((ynew,xnew))
    return listtoret

def findthebestmove(pos):
    global moves

    for i in range(1, len(moves[pos])):
        p = moves[pos][i]
        if p[0] == p[1] == 0 or p[0] == p[1] == boardSize - 1 or \
           (p[0] == 0 and p[1] == boardSize - 1) or (p[0] == boardSize - 1 and p[1] == 0):
            return moves[pos].pop(i)

    for i in range(1, len(moves[pos])):
        p = moves[pos][i]
        if p[0] == 0 or p[0] == boardSize - 1 or p[1] == 0 or p[1] == boardSize - 1:
            return moves[pos].pop(i)
    for i in range(1, len(moves[pos])):
        p = moves[pos][i]
        if p[0] == 1 or p[0] == boardSize - 2 or p[1] == 1 or p[1] == boardSize - 2:
            return moves[pos].pop(i)

    for i in range(1, len(moves[pos])):
        p = moves[pos][i]
        if p[0] == 2 or p[0] == boardSize - 3 or p[1] == 2 or p[1] == boardSize - 3:
            return moves[pos].pop(i)

    if boardSize > 6:
        for i in range(1, len(moves[pos])):
            p = moves[pos][i]
            if p[0] == 3 or p[0] == boardSize - 4 or p[1] == 3 or p[1] == boardSize - 4:
                return moves[pos].pop(i)
    return moves[pos].pop()


def gobacktoprev((y,x)):
    global moves,board,visited
    moves.pop()
    visited-=1
    board[y][x]=''
    if len(moves)>0:
        knight= (moves[-1][-1])
        board[knight[0]][knight[1]]= ''
        return
    else:
        print "Backtracked off the board"


findclosedtour()


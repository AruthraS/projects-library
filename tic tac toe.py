#1-win
#0-draw
#-1-continue
board=dict([(i,' ') for i in range(1,10)])
def draw():
    print(" _________________")
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(board[1],board[2],board[3]))
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(board[4],board[5],board[6]))
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(board[7],board[8],board[9]))
    print("|_____|_____|_____|")
def check():
    #horizontal
    if (board[1]!=" ") and(board[1]==board[2]) and (board[1]==board[3]):
        return 1
    elif (board[4]!=" ") and(board[4]==board[5]) and (board[4]==board[6]):
        return 1
    elif (board[7]!=" ") and(board[7]==board[8]) and (board[7]==board[9]):
        return 1
    #vertical
    elif (board[1]!=" ") and(board[1]==board[4]) and (board[1]==board[7]):
        return 1
    elif (board[2]!=" ") and(board[2]==board[5]) and (board[2]==board[8]):
        return 1
    elif (board[3]!=" ") and(board[3]==board[6]) and (board[3]==board[9]):
        return 1
    #diagonal
    elif (board[1]!=" ") and(board[1]==board[5]) and (board[1]==board[9]):
        return 1
    elif (board[3]!=" ") and(board[3]==board[5]) and (board[3]==board[7]):
        return 1
    #draw
    elif board[1]!=" " and board[2]!=" " and board[3]!=" " and board[4]!=" " and board[5]!=" " and board[6]!=" " and board[7]!=" " and board[8]!=" " and board[9]!=" ":
        return 0
    #continue
    return -1
i=-1
j=1
while i==-1:
    draw()
    if j==1:
        print("PLAYER 1(X) TURN")
        print("CHOICES SHOULD BE FROM 1 TO 9")
        c=int(input("ENTER YOUR CHOICE: "))
        board[c]="X"
        i=check()
        j=2
    elif j==2:
        print("PLAYER 2(O) TURN")
        print("CHOICES SHOULD BE FROM 1 TO 9")
        c=int(input("ENTER YOUR CHOICE: "))
        board[c]="O"
        i=check()
        j=1
draw()
if i==1:
    if j==2:
        print("PLAYER 1 WINS")
    else:
        print("PLAYER 2 WINS")
else:
    print("DRAW")

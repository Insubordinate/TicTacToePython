#this creates the board as a series of variables with number assigned to them; 
#the appropriate x/o or empty value assigned to it.
#hooplah
a="1"
b="2"
c="3"
d="4"
e="5"
f="6"
g="7"
h="8"
i="9"
goodTurn=1;
moves=1;
won=False;
def displayBoard():
 Activeboard = "%s | %s | %s\n______\n%s | %s | %s \n______\n%s | %s | %s" % (a,b,c,d,e,f,g,h,i)
 print Activeboard;
def whoseTurn():
    if(moves%2!=0):
        return "X"
    else:
        return "O"
def validMove(letter):
    if(letter == "X" or letter == "O"):
        print "That square is already taken!\nTry again.\n"
        global goodTurn
        goodTurn = 0
        return False
    else:
        global goodTurn
        goodTurn = 1
        return True
def checkForWin():
    if(a==b and b==c):
        return True
    elif(d==e and e==f):
        return True
    elif(g==h and h==i):
        return True
    elif(a==d and d==g):
        return True
    elif(b==e and e==h):
        return True
    elif(c==f and f==i):
        return True
    elif(a==e and e==i):
        return True
    elif(c==e and e==g):
        return True
def changeSquare():
    changer=input("Enter a square to change:  ")
    player = whoseTurn();
    if(changer==1 and validMove(a)):
        global a
        a= player
    elif(changer==2 and validMove(b)):
        global b
        b = player
    elif(changer==3 and validMove(c)):
        global c
        c = player
    elif(changer==4 and validMove(d)):
        global d
        d = player
    elif(changer==5 and validMove(e)):
        global e
        e = player
    elif(changer==6 and validMove(f)):
        global f
        f = player
    elif(changer==7 and validMove(g)):
        global g
        g = player
    elif(changer==8 and validMove(h)):
        global h
        h = player
    elif(changer==9 and validMove(i)):
        global i
        i = player

while moves!=10 and won!=True:
    displayBoard();
    changeSquare();
    won = checkForWin();
    if(goodTurn):
        moves+=1
if(won):
    print "Congratulations Player %s, you won!\n" %(whoseTurn())
    displayBoard();
else:
    print "The game is a tie.\n"
    displayBoard();

    

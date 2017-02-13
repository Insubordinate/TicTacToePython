#this creates the board as a series of variables with number assigned to them; 
#the appropriate x/o or empty value assigned to it.

a="1"
b="2"
c="3"
d="4"
e="5"
f="6"
g="7"
h="8"
i="9"

moves=1;
won=False;
def displayBoard():
 Activeboard = "%s | %s | %s\n%s | %s | %s \n%s | %s | %s" % (a,b,c,d,e,f,g,h,i)
 print Activeboard;


def changeSquare():
	changer=input("Enter a square to change:  ")
	if(changer==1):
		global a
		a="X"
	if(changer==2):
		global b
		b ="X"
	if(changer==3):
		global c
		c = "X"
	if(changer==4):
		global d
		d = "X"
	if(changer==5):
		global e
		e = "X"
	if(changer==6):
		global f
		f = "X"
	if(changer==7):
		global g
		g = "X"
	if(changer==8):
		global h
		h = "X"
	if(changer==9):
		global i
		i = "X"

while moves!=10 and won!=True:
	displayBoard();
	changeSquare();
	moves+=1;


displayBoard()

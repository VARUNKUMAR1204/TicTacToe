from tkinter import *
from time import sleep as s 

plays = 0
turn = "X"
xs=[]
os=[]

def clicked(b):
	global turn,plays,xs,os
	if b["text"] == '':	
		b.configure(text = turn)
		plays += 1
		if turn == "X":

			turn = "O"
		else:
			turn = "X"
		if plays%9 == 0 or checkwin() :
			turn = "X"
			plays = 0
			reset()

def checkwin():
	flag = False
	if b1["text"]==b2["text"] and b1["text"] == b3["text"] and b1["text"] != '':
		print(b1["text"],end = ' WON!')
		return True
	if b4["text"]==b5["text"] and b4["text"] == b6["text"] and b4["text"] != '':
		print(b1["text"],end = ' WON!')
		return True
	if b7["text"]==b8["text"] and b7["text"] == b9["text"] and b7["text"] != '':
		print(b1["text"],end = ' WON!')
		return True
	if b1["text"]==b4["text"] and b4["text"] == b7["text"] and b1["text"] != '':
		print(b1["text"],end = ' WON!')
		return True
	if b2["text"]==b5["text"] and b5["text"] == b8["text"] and b2["text"] != '':
		print(b1["text"],end = ' WON!')
		return True
	if b3["text"]==b6["text"] and b6["text"] == b9["text"] and b3["text"] != '':
		print(b1["text"],end = ' WON!')
		return True
	if b1["text"]==b5["text"] and b1["text"] == b9["text"] and b1["text"] != '':
		print(b1["text"],end = ' WON!')
		return True
	if b3["text"]==b5["text"] and b5["text"] == b7["text"] and b3["text"] != '':
		print(b1["text"],end = ' WON!')
		return True

def reset():
	b1.configure(bg = "white",text = '')
	b2.configure(bg = "white",text = '')
	b3.configure(bg = "white",text = '')
	b4.configure(bg = "white",text = '')
	b5.configure(bg = "white",text = '')
	b6.configure(bg = "white",text = '')
	b7.configure(bg = "white",text = '')
	b8.configure(bg = "white",text = '')
	b9.configure(bg = "white",text = '')



win = Tk()

b1 = Button(win,text = '',bg = "white",width = 16, height = 8 , command = lambda : clicked(b1))
b2 = Button(win,text = '',bg = "white",width = 16, height = 8 , command = lambda : clicked(b2))
b3 = Button(win,text = '',bg = "white",width = 16, height = 8 , command = lambda : clicked(b3))
b4 = Button(win,text = '',bg = "white",width = 16, height = 8 , command = lambda : clicked(b4))
b5 = Button(win,text = '',bg = "white",width = 16, height = 8 , command = lambda : clicked(b5))
b6 = Button(win,text = '',bg = "white",width = 16, height = 8 , command = lambda : clicked(b6))
b7 = Button(win,text = '',bg = "white",width = 16, height = 8 , command = lambda : clicked(b7))
b8 = Button(win,text = '',bg = "white",width = 16, height = 8 , command = lambda : clicked(b8))
b9 = Button(win,text = '',bg = "white",width = 16, height = 8 , command = lambda : clicked(b9))

b1.grid(row = 1, column = 1)
b2.grid(row = 1, column = 2)
b3.grid(row = 1, column = 3)
b4.grid(row = 2, column = 1)
b5.grid(row = 2, column = 2)
b6.grid(row = 2, column = 3)
b7.grid(row = 3, column = 1)
b8.grid(row = 3, column = 2)
b9.grid(row = 3, column = 3)

win.mainloop()
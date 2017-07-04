from tkinter import *
import time
import random

speed = 0.3
val = 3


def set_speed():
	global speed
	speed = float(my_speed.get())
	r1.destroy()
	r2.destroy()
	r3.destroy()


def show(num):
	if num == 123 or num == 213:
		joker1.config(image=joker_img)
		joker2.config(image=joker_img)
		ace.config(image=ace_img)
	if num == 132 or num == 231:
		joker1.config(image = joker_img)
		joker2.config(image = ace_img)
		ace.config(image = joker_img)
	if num == 321 or num == 312:
		joker1.config(image = ace_img)
		joker2.config(image = joker_img)
		ace.config(image = joker_img)
		
	txtlb = Label(root, text="3", bg="black", fg="red", font=("Times", 36))
	txtlb.grid(row=3, column=1, padx=10, pady=25)
	root.update()
	time.sleep(1)
	txtlb.config(text="2", font=("Times", 32), fg="yellow")
	root.update()
	time.sleep(1)
	txtlb.config(text = "1", font=("Times", 26), fg="green")
	root.update()
	time.sleep(1)
	txtlb.config(text = "START", font=("Times", 28), fg="green")
	root.update()
	joker1.config(image=back_img)
	joker2.config(image=back_img)
	ace.config(image=back_img)
	txtlb.destroy()
	time.sleep(1)
	root.update()


def func13():
	global val, speed
	
	joker1.after(1000, lambda: joker1.config(image=black_img))
	l1.after(1000, lambda: l1.config(image=back_img))
	
	ace.after(1000, lambda: ace.config(image = black_img))
	l3.after(1000, lambda: l3.config(image = back_img))

	time.sleep(speed)
	root.update()
	
	l1.after(1000, lambda: l1.config(image=black_img))
	l2.after(1000, lambda: l2.config(image=back_img))
	
	l3.after(1000, lambda: l3.config(image = black_img))
	l2.after(1000, lambda: l2.config(image = back_img))
	
	time.sleep(speed)
	root.update()
	
	l2.after(1000, lambda: l2.config(image=black_img))
	l3.after(1000, lambda: l3.config(image=back_img))
	l1.after(1000, lambda: l1.config(image = back_img))
	
	time.sleep(speed)
	root.update()
	
	l3.after(1000, lambda: l3.config(image = black_img))
	ace.after(1000, lambda: ace.config(image = back_img))
	
	l1.after(1000, lambda: l1.config(image = black_img))
	joker1.after(1000, lambda: joker1.config(image = back_img))
	
	time.sleep(speed)
	root.update()
	
	if val == 1:
		val = 3
	elif val == 3:
		val = 1
	else:
		pass


def func12():
	global val, speed
	
	joker1.after(1000, lambda: joker1.config(image=black_img))
	l1.after(1000, lambda: l1.config(image=back_img))
	
	time.sleep(speed)
	root.update()
	
	l1.after(1000, lambda: l1.config(image=black_img))
	l2.after(1000, lambda: l2.config(image=back_img))
	
	time.sleep(speed)
	root.update()
	
	joker2.after(1000, lambda: joker2.config(image=black_img))
	joker1.after(1000, lambda: joker1.config(image=back_img))
	
	time.sleep(speed)
	root.update()
	
	l2.after(1000, lambda: l2.config(image=black_img))
	joker2.after(1000, lambda: joker2.config(image=back_img))
	
	time.sleep(speed)
	root.update()
	
	if val == 1:
		val = 2
	elif val == 2:
		val = 1
	else:
		pass


def func23():
	global val, speed
	joker2.after(1000, lambda: joker2.config(image=black_img))
	l2.after(1000, lambda: l2.config(image=back_img))
	
	time.sleep(speed)
	root.update()
	
	l2.after(1000, lambda: l2.config(image=black_img))
	l3.after(1000, lambda: l3.config(image=back_img))
	
	time.sleep(speed)
	root.update()
	
	ace.after(1000, lambda: ace.config(image=black_img))
	joker2.after(1000, lambda: joker2.config(image=back_img))
	
	time.sleep(speed)
	root.update()
	
	l3.after(1000, lambda: l3.config(image=black_img))
	ace.after(1000, lambda: ace.config(image=back_img))
	
	time.sleep(speed)
	root.update()
	
	if val == 2:
		val = 3
	elif val == 3:
		val = 2
	else:
		pass


def answer(num):
	
	if num == 3:
		joker1.config(image=joker_img)
		joker2.config(image = joker_img)
		ace.config(image = ace_img)
	if num == 2:
		joker1.config(image = joker_img)
		joker2.config(image = ace_img)
		ace.config(image = joker_img)
	if num == 1:
		joker1.config(image = ace_img)
		joker2.config(image = joker_img)
		ace.config(image = joker_img)
	
	
def func():
	show(123)
	for i in range(0, 20):
		r = random.randint(0, 2)
		if r == 0:
			func12()
		elif r == 1:
			func23()
		else:
			func13()


def check1():
	global val
	if val == 1:
		label.config(text="YOU WON!!!", fg="yellow")
	else:
		label.config(text = "YOU LOST!!!", fg="red")
	answer(val)
	
	
def check2():
	global val
	if val == 2:
		label.config(text="YOU WON!!!", fg="yellow")
	else:
		label.config(text = "YOU LOST!!!", fg="red")
	answer(val)
	
	
def check3():
	global val
	if val == 3:
		label.config(text="YOU WON!!!", fg="yellow")
	else:
		label.config(text = "YOU LOST!!!", fg="red")
	answer(val)
	

root = Tk()
root.config(bg="black")
my_speed = DoubleVar()
label = Label(root, text = "IDENTIFY WHERE THE ACE CARD IS!!!", fg="white", bg="black")
r1 = Radiobutton(root, text="Easy", value=0.3, variable=my_speed, command=set_speed, fg="white", bg="black")
r2 = Radiobutton(root, text="Medium", value=0.2, variable=my_speed, command=set_speed, fg="white", bg="black")
r3 = Radiobutton(root, text="Hard", value=0.1, variable=my_speed, command=set_speed, fg="white", bg="black")
r1.grid(row=1, column=0)
r2.grid(row=1, column=1)
r3.grid(row=1, column=2)
joker_img = PhotoImage(file = "joker.gif")
ace_img = PhotoImage(file = "ace.gif")
back_img = PhotoImage(file = "back.gif")
white_img = PhotoImage(file = "white.gif")
black_img = PhotoImage(file="black.gif")

joker1 = Label(root, image = back_img, fg="white", bg="black", width = 100, height = 150)
joker2 = Label(root, image = back_img, fg="white", bg="black", width = 100, height = 150)
ace = Label(root, image = back_img, fg="white", bg="black", width = 100, height = 150)
l1 = Label(root, image = black_img, fg="white", bg="black", width = 100, height = 150)
l2 = Label(root, image = black_img, fg="white", bg="black", width = 100, height = 150)
l3 = Label(root, image = black_img, fg="white", bg="black", width = 100, height = 150)

label.grid(row = 0, columnspan = 3, padx=5, pady=5)

# joker1.photo = back_img
joker1.grid(row = 2, column = 0, padx = 25, pady=10)

# joker2.photo = back_img
joker2.grid(row = 2, column = 1, padx = 25, pady=10)

# ace.photo = back_img
ace.grid(row = 2, column = 2, padx = 25, pady=10)

# l1.photo = black_img
l1.grid(row = 3, column = 0, padx = 25, pady=10)

# l2.photo = black_img
l2.grid(row = 3, column = 1, padx = 25, pady=10)

# l3.photo = black_img
l3.grid(row = 3, column = 2, padx = 25, pady=10)

bl1 = Button(root, text="1st CARD", fg="white", bg="black", command=check1).grid(row=4, column=0, padx=10, pady=10)
bl2 = Button(root, text="2nd CARD", fg="white", bg="black", command=check2).grid(row=4, column=1, padx=10, pady=10)
bl3 = Button(root, text="3rd CARD", fg="white", bg="black", command=check3).grid(row=4, column=2, padx=10, pady=10)

b1 = Button(root, text="START", command=func, fg="white", bg="black")
b1.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()


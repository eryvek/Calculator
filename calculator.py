from tkinter import *
lab_str_x = ''
lab_str_y = ''
op = ''


def setx(m):
    if op =='':
        global lab_str_x
        lab_str_x += str(m)
        label.configure(text=lab_str_x)
        print("Value of x set to : " + lab_str_x)
    else:
        sety(m)


def sety(m):
    global lab_str_y
    lab_str_y += str(m)
    label.configure(text=lab_str_y)
    print("Value of y set to : " + lab_str_y)
    '''if (op=='+'):
        addition(int(lab_str_x),int(lab_str_y))
    elif (op=='-'):
        subtract(int(lab_str_x),int(lab_str_y))
    elif (op=='X'):
        multiplication(int(lab_str_x),int(lab_str_y))
    elif (op=='/'):
        division(int(lab_str_x),int(lab_str_y))'''



def addition(x,y):
    global res
    res = x+y


def subtract(x,y):
    global res
    res = x-y


def multiplication(x,y):
    global res
    res = x*y


def division(x,y):
    global res
    if (y==0):
        label.configure(text='Division by zero is not Possible sir')
    else:
        res = x/y


def show():
    print("Show function called addition performed")
    if op =='+':
        print("Addition performed")
        addition(int(lab_str_x),int(lab_str_y))
        label.configure(text=res)
    elif op=='-':
        print("Subtraction performed")
        subtract(int(lab_str_x), int(lab_str_y))
        label.configure(text=res)
    elif op == 'X':
        print("Multiplication performed")
        multiplication(int(lab_str_x), int(lab_str_y))
        label.configure(text=res)
    elif op == '/':
        print("Division performed")
        division(int(lab_str_x), int(lab_str_y))
        label.configure(text=res)


def clear():
    label.configure(text='')
    global x, y, op, lab_str_y,lab_str_x
    op = ''
    lab_str_y = ''
    lab_str_x = ''


def set_op(s):
    global op
    op = s
    label.configure(text=op)
    print(op)


root = Tk()

display_frame = Frame()
display_frame.pack()
label = Label(display_frame,width=25,text="")
label.pack(pady=10)

number_frame = Frame()
number_frame.pack()

plus = Button(number_frame, text="+",width=4,height=2,command=lambda : set_op('+'))
button1 = Button(number_frame, text="1",width=4,height=2,command=lambda :setx(1))
button2 = Button(number_frame, text="2",width=4,height=2,command=lambda :setx(2))
button3 = Button(number_frame, text="3",width=4,height=2,command=lambda :setx(3))

plus.grid(row=1,column=0,)
button1.grid(row=1,column=1)
button2.grid(row=1,column=2)
button3.grid(row=1,column=3)

minus = Button(number_frame, text="-",width=4,height=2,command=lambda :set_op('-'))
button4 = Button(number_frame, text="4",width=4,height=2,command=lambda :setx(4))
button5 = Button(number_frame, text="5",width=4,height=2,command=lambda :setx(5))
button6 = Button(number_frame, text="6",width=4,height=2,command=lambda :setx(6))

minus.grid(row=2,column=0,)
button4.grid(row=2,column=1)
button5.grid(row=2,column=2)
button6.grid(row=2,column=3)

multiply = Button(number_frame, text="X",width=4,height=2,command=lambda : set_op('X'))
button7 = Button(number_frame, text="7",width=4,height=2,command=lambda :setx(7))
button8 = Button(number_frame, text="8",width=4,height=2,command=lambda :setx(8))
button9 = Button(number_frame, text="9",width=4,height=2,command=lambda :setx(9))

multiply.grid(row=3,column=0,)
button7.grid(row=3,column=1)
button8.grid(row=3,column=2)
button9.grid(row=3,column=3)

divide = Button(number_frame, text="/",width=4,height=2,command=lambda : set_op('/'))
button0 = Button(number_frame, text="0",width=4,height=2,command=lambda :setx(0))
equal = Button(number_frame, text="=",width=4,height=2,command=lambda : show())
clear_btn = Button(number_frame, text="AC",width=4,height=2,command=lambda : clear())

divide.grid(row=4,column=0)
equal.grid(row=4,column=1)
button0.grid(row=4,column=2)
clear_btn.grid(row=4,column=3)


status = Label(root,text="Anurag's Calculator...",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X,pady=0)


root.mainloop()
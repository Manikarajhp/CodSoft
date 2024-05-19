from tkinter import *
from tkinter import messagebox
win=Tk()
win.geometry("400x620")
Font=("Ariel",22,"bold")
frm1=Frame(win,bg="blue",width=400,height=50)
frm1.pack()#Title frame
title_lab=Label(frm1,bg="blue",text="SIMPLE CALCULATOR",fg="white",font=Font)
title_lab.place(x=50,y=10)

expression=''
frm2=Frame(win,bg='white',width=400,height=100)
frm2.pack()#Answer frame
lab1=Label(frm2,font=Font,text=expression,bg="white")
lab1.place(x=0,y=20)

def add(x):
    global expression,lab1
    if expression.lower()=="error" or expression.lower()=="invalid input":
        lab1.destroy()
        expression=''
    if x=="=":
        lab1.destroy()
        for i in expression:
            if i=="/":
                try:
                    if expression[expression.index(i)+1]=="0":
                        expression="ERROR"
                except:
                    expression="Invalid Input"
        else:
            try:
                expression=str(eval(expression))
            except:
                expression="Invalid Input"
    elif x=="c":
        lab1.destroy()
        expression=expression[:len(expression)-1]
    elif x=="ac":
        lab1.destroy()
        expression=''
    else:
        lab1.destroy()
        expression+=x
    lab1=Label(frm2,font=Font,text=expression,bg="white")
    lab1.place(x=0,y=20)



frm3=Frame(win,width=400,height=500)
frm3.pack()
clear_btn=Button(frm3,text="C",width=5,height=2,font=Font,command=lambda:add("c"))
all_btn=Button(frm3,text="AC",width=5,height=2,font=Font,command=lambda:add("ac"))
quit_btn=Button(frm3,text="OFF",width=5,height=2,font=Font,command=quit)
mod_btn=Button(frm3,text="%",width=5,height=2,font=Font,command=lambda:add("%"))
seven_btn=Button(frm3,text="7",width=5,height=2,font=Font,command=lambda:add("7"))
eight_btn=Button(frm3,text="8",width=5,height=2,font=Font,command=lambda:add("8"))
nine_btn=Button(frm3,text="9",width=5,height=2,font=Font,command=lambda:add("9"))
divi_btn=Button(frm3,text="/",width=5,height=2,font=Font,command=lambda:add("/"))
four_btn=Button(frm3,text="4",width=5,height=2,font=Font,command=lambda:add("4"))
five_btn=Button(frm3,text="5",width=5,height=2,font=Font,command=lambda:add("5"))
six_btn=Button(frm3,text="6",width=5,height=2,font=Font,command=lambda:add("6"))
multi_btn=Button(frm3,text="x",width=5,height=2,font=Font,command=lambda:add("*"))
one_btn=Button(frm3,text="1",width=5,height=2,font=Font,command=lambda:add("1"))
two_btn=Button(frm3,text="2",width=5,height=2,font=Font,command=lambda:add("2"))
three_btn=Button(frm3,text="3",width=5,height=2,font=Font,command=lambda:add("3"))
minus_btn=Button(frm3,text="-",width=5,height=2,font=Font,command=lambda:add("-"))
zero_btn=Button(frm3,text="0",width=5,height=2,font=Font,command=lambda:add("0"))
dot_btn=Button(frm3,text=".",width=5,height=2,font=Font,command=lambda:add("."))
equal_btn=Button(frm3,text="=",width=5,height=2,font=Font,command=lambda:add("="))
plus_btn=Button(frm3,text="+",width=5,height=2,font=Font,command=lambda:add("+"))
BUTTONS=[clear_btn,all_btn,quit_btn,mod_btn,seven_btn,eight_btn,nine_btn,divi_btn,four_btn,five_btn,six_btn,multi_btn,one_btn,two_btn,three_btn,minus_btn,zero_btn,dot_btn,equal_btn,plus_btn]
btn=0
for i in range(0,5):
    for j in range(0,4):
        BUTTONS[btn].grid(row=i,column=j)
        btn+=1
win.mainloop()

from tkinter import *
import pyperclip
from tkinter import messagebox
import random

win=Tk()
win.geometry("400x400")
win.configure(bg="lightblue")
selected_pass=''
def pass_gene(n):
    global selected_pass
    if int(n)>20 or int(n)<5:
        messagebox.showinfo("Alert","You can enter length of password between 5-20.")
    else:
        ent2.delete(0,END)
        ascii_list=list(range(33,123))
        pswrd=[]
        for i in [96,94,61,58,46,45,44,39,34]:
            if i in ascii_list:
                ascii_list.remove(i)
        for i in range(int(n)):
            xrand=random.choice(ascii_list)
            pswrd.append(chr(xrand))
        random.shuffle(pswrd)
        password=''.join(pswrd)
        selected_pass=password
        ent2.insert(0,password)
#BELOW FUNCTION IS TO COPY THE PASSWORD.
def coping():
    pyperclip.copy(selected_pass)
    messagebox.showinfo("Successfull","Password copied.")
    
lab1=Label(win,text="Password Generator",bg="lightblue",font=("Arial",22,"bold"))
lab1.pack()
frm1=Frame(win,width=500,height=50,bg="lightblue")
frm1.pack()
lab2=Label(frm1,text="Length of Password:",bg="lightblue",font=("Arial",12,"bold"))
lab2.grid(row=0,column=0)
#to get the length of password
ent1=Entry(frm1,width=20)
ent1.grid(row=0,column=1)
#generate button
btn1=Button(win,text="Generate",bg="lightblue",command=lambda:pass_gene(ent1.get()))
btn1.pack()

lab3=Label(win,text="Your Password",bg="lightblue")
lab3.pack()
frm2=Frame(win,width=500,height=50,bg="lightblue")
frm2.pack()
#to show the password
ent2=Entry(frm2,width=30)
ent2.grid(row=0,column=0)
span1=Label(frm2,text="     ",bg="lightblue")
span1.grid(row=0,column=1)
btn2=Button(frm2,width=4,bg="lightblue",text="copy",command=coping)
btn2.grid(row=0,column=2)
win.mainloop()

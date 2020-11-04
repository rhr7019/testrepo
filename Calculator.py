import tkinter as tk
def product():
    n1=e1.get()
    n2=e2.get()
    display=str(int(n1)*int(n2))
    l2['text']=display
def sum1():
    n1=e1.get()
    n2=e2.get()
    display=str(int(n1)+int(n2))
    l2['text']=display
def diff():
    n1=e1.get()
    n2=e2.get()
    display=str(int(n1)-int(n2))
    l2['text']=display
def quo():
    n1=e1.get()
    n2=e2.get()
    displaystr(int(n1)//int(n2))
    l2['text']=display
def clear():
    l2['text']='  '
top=tk.Tk()
top.title("Calculator")
l1=tk.Label(top,fg='red',text="calculator for 2 number")
e1=tk.Entry(top,fg='red')
e2=tk.Entry(top,fg='blue')
b1=tk.Button(top,text="Show Product",command=product)
b2=tk.Button(top,text="Show Sum",command=sum1)
b3=tk.Button(top,text="Show Difference",command=diff)
b4=tk.Button(top,text="Show Quotient",command=quo)
b5=tk.Button(top,text="Clear Screen",command=clear)
button=tk.Button(top,text="Exit",command=top.destroy)
l2=tk.Label(top,fg="black")
l1.pack()
l2.pack()
e1.pack()
e2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
button.pack()
top.mainloop()

from tkinter import *
import random

def setLab():
    x1,x2,x3,x4,x5,x6=random.sample(range(1,122),6)

    labl.config(text=x1)
    labl1.config(text=x2)
    labl2.config(text=x3)
    labl3.config(text=x4)
    labl4.config(text=x5)
    labl5.config(text=x6)

window=Tk()
window.title("Thired Python window")
window.geometry("1100x600+100+50") 
window.config(bg="red") 

labl=Label(window, text=0,width=20,height=3,bg="yellow")
labl.pack()
labl1=Label(window, text=0,width=20,height=3,bg="yellow")
labl1.pack()
labl2=Label(window, text=0,width=20,height=3,bg="yellow")
labl2.pack()
labl3=Label(window, text=0,width=20,height=3,bg="yellow")
labl3.pack()
labl4=Label(window, text=0,width=20,height=3,bg="yellow")
labl4.pack()
labl5=Label(window, text=0,width=20,height=3,bg="yellow")
labl5.pack()

btnrandom=Button(window,text="Generate", command=setLab)
btnrandom.pack()

btnExit=Button(window, text="Exit", command=window.destroy) 
btnExit.pack() 

window.mainloop()

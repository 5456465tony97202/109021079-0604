from tkinter import *
import random

def serLab():
    global x
    x=random.randint(1,100)
    labl.config(text=x)

window=Tk()
window.title("Second Python window")
window.geometry("400x600+100+50") 
window.config(bg="blue") 

labl=Label(window, text="^_^",width=20,height=3,bg="red")
labl.pack()

btnrandom=Button(window,text="Generate", command=serLab)
btnrandom.pack()

btnExit=Button(window, text="Exit", command=window.destroy) 
btnExit.pack() 

window.mainloop()

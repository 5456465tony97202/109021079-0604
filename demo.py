from tkinter import *
import tkinter
x=int(input())

def addLab():
    global x
    x=x*2
    labl.config(text=x)
def subLab():
    global x
    x=x-20
    labl.config(text=x)




window=tkinter.Tk()
window.title("First Python window")
window.geometry("600x400+100+50") #座標 +100+50 營幕位移
window.config(bg="green") #背景顏色

labl=Label(window, text=x,width=12,height=3,bg="yellow")
labl.pack()

addBtn=Button(window, text="+1", command=addLab)
addBtn.pack()

subBtn=Button(window, text="-1", command=subLab)
subBtn.pack()

btnExit=Button(window, text="Exit", command=window.destroy) #建立關閉視窗的按鍵
btnExit.pack() #放進視窗裡

window.mainloop()


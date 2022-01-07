from tkinter import*
from math import*
import matplotlib.pyplot as plt
import numpy as np
global knipka,kp,kop
def lahenda():
    if (knipka.get()!="" and kp.get()!="" and kop.get()!=""):
        knipka_=float(knipka.get())
        kp_=float(kp.get())
        kop_=float(kop.get())
        D=kp_*kp_-4*knipka_*kop_
        if D>0:
            x1_=round((-1*kp_+sqrt(D))/(2*knipka_),2)
            x2_=round((-1*kp_-sqrt(D))*(2*knipka_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            graf=True
        elif D==0:
            x1_round((-1*kp_)/(2*knipka_),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="Нет корней"
            graf=False
        otvet.configure(text=f"D={D}\n{t}")
        knipka.configure(bg="lightblue")
        kp.configure(bg="lightblue")
        kop.configure(bg="lightblue")
    else:
        if knipka.get()=="":
            knipka.configure(bg="red")
        if kp.get()=="":
            kp.configure(bg="red")
        if kop.get()=="":
            kop.configure(bg="red")
    return graf,D,t
def graafik():
    graf,D,t=lahenda()
    if graf==True:
        knipka_=int(knipka.get())
        kp_=int(kp.get())
        kop_=int(kop.get())
        x0=(-kp_)/(2*knipka_)
        y0=knipka_*x0*x0+kp_*x0+kop_
        x = np.arange(x0-10, x0+10, 0.5)
        y=knipka_*x*x+kp_*x+kop_
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    otvet.configure(text=f"D={D}\n{t}\n{text}")

aken=Tk()
aken.title("Решение квадратного уравнения")
aken.geometry("800x400")
reshen=Label(aken,text="решение квадратного уровнения",font="Arial 18",fg="green",bg="lightblue",height=2,width=30,relief=GROOVE)
otvet=Label(aken,text="ответ", height=4,width=60,bg="yellow")
knipka=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=5)
ll=Label(aken,text="x**2+",font="Arial 20", fg="green",)
kp=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=5)
knipx=Label(aken,text="x+",font="Arial 20", fg="green")
kop=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=5)
pop=Label(aken,text="=0",font="Arial 20", fg="green")
kit=Button(aken,text="Решить",font="Arial 20",bg="green",command=lahenda)
kot_g=Button(aken,text="График", font="Arial 20",bg="green",command=graafik)
rad1=Radiobutton(aken,text="kit", font="Arial 20",bg="green",command=graafik)
rad2=Radiobutton(aken,text="zontik", font="Arial 20",bg="green",command=graafik)
rad3=Radiobutton(aken,text="laguska", font="Arial 20",bg="green",command=graafik)



rad3.pack()
rad2.pack()
rad1.pack()
kot_g.pack(side=RIGHT)
kit.pack(side=LEFT)
reshen.pack()
otvet.pack(side=BOTTOM)
knipka.pack(side=LEFT)
ll.pack(side=LEFT)
kp.pack(side=LEFT)
knipx.pack(side=LEFT)
kop.pack(side=LEFT)
pop.pack(side=LEFT)
kit.pack(side=RIGHT)




aken.mainloop()

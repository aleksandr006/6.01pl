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
    flag,D,t=lahenda()
    if flag==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,"b:o", x0, y0,"g-d")
        plt.title("Квадратное уравнение")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.grid(True)
        plt.show()
        text=f"вершина параболы({x0},{y0})"
    else:
        text=f"график нет возможности построить"
    otv.configure(text=f"D={D}\n{t}\n{text}")
t=0
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        uvokno.config(text="Уменьшить окно")
        t=1
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        uvokno.config(text="Увеличить окно")
        t=0
def kittt():
    x1=np.arange(0,9.5,0.5)
    y1=(2/27)*x1*x1-3 
    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2*x2-3 
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6 
    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=np.arange(5,8.3,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-9.5,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    fig=plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('square equation')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
       
def o4ki():
    x1=np.arange(-9,-1,0.5)
    y1=(-1/16)*(x1+5)**2+2
    x2=np.arange(1,9,0.5)
    y2=(-1/16)*(x2-5)**2+2
    x3=np.arange(-9,-1,0.5)
    y3=1/4*(x3+5)**2-3
    x4=np.arange(1,9,0.5)
    y4=1/4*(x4-5)**2-3
    x5=np.arange(-9,-6,0.5)
    y5=-(x5+7)**2+5
    x6=np.arange(6,9,0.5)
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1,0.5)
    y7=(-0.5)*x7*x7+1.5
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title('Очки')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
    
def zont():
    x1=np.arange(-12,12,0.5)
    y1=(-1/18)*x1*x1+12
    x2=np.arange(-4,4,0.5)
    y2=(-1/8)*x2*x2+6
    x3=np.arange(-12,-4,0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=np.arange(4,12,0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=np.arange(-4,-0.3,0.5)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,0.2,0.5)
    y6=1.5*(x6+3)**2-10
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title('Зонтик')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
    


aken=Tk()
aken.title("Решение квадратного уравнения")
aken.geometry("800x400")
f1=Frame(aken,width=650,height=200)
f1.pack(side=TOP)
f2=Frame(aken,width=650,height=200)
f2.pack(side=BOTTOM)
reshen=Label(f1,text="решение квадратного уровнения",font="Arial 18",fg="green",bg="lightblue",height=2,width=30,relief=GROOVE)
otvet=Label(f1,text="ответ", height=4,width=60,bg="yellow")
knipka=Entry(f1,font="Arial 20", fg="green",bg="lightblue",width=5)
ll=Label(f1,text="x**2+",font="Arial 20", fg="green",)
kp=Entry(f1,font="Arial 20", fg="green",bg="lightblue",width=5)
knipx=Label(f1,text="x+",font="Arial 20", fg="green")
kop=Entry(f1,font="Arial 20", fg="green",bg="lightblue",width=5)
pop=Label(f1,text="=0",font="Arial 20", fg="green")
kit=Button(f1,text="Решить",font="Arial 20",bg="green",command=lahenda)
kot_g=Button(f1,text="График", font="Arial 20",bg="green",command=graafik)
rad1=Radiobutton(f2,text="o4ki", font="Arial 20",bg="green",command=o4ki)
rad2=Radiobutton(f2,text="zont", font="Arial 20",bg="green",command=zont)
rad3=Radiobutton(f2,text="kit", font="Arial 20",bg="green",command=kittt)
uvokno=Button(f2,text="uvel okno",font="Arial 20",bg="green",command=veel)




uvokno.pack()
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


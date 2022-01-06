from tkinter import *




aken=Tk()
aken.title("Akna nimetus")
aken.geometry("800x400")
nupp=Label(aken,text="решение квадратного уровнения",font="Arial 20",fg="green",bg="lightblue",height=2,width=30,relief=GROOVE)
knopka=Label(aken,text="решение",font="Arial 20",fg="black",bg="lightgreen",height=2,width=10,relief=GROOVE,)
txt=Entry(aken,width=10,relief=GROOVE,bg="lightblue",justify=CENTER)
nup=Button(aken,text="D=8\nX1=1.71,\nX2=0.29",font="Arial 20",fg="black",bg="lightyellow",height=2,width=30,relief=GROOVE)


nup.pack()
nupp.pack()
knopka.pack(side=RIGHT)
txt.pack(side=LEFT)
aken.mainloop()
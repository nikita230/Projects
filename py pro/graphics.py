from tkinter import *
import sqlite3 as sqlite3
master = Tk() 
frametop=Frame(master)
master.configure(bg="#cc0066")
frametop.pack()
frame=Frame(master)
frame.configure(bg="#cc0066")
frame.place(relx=0.5,rely=0.5,anchor='center')    

def callemergency():
    import emergency
def callentry():
    import entry
def callnormal():
    import normal
    
ourmsg="SELECT YOUR CHOICE"
msg=Message(master,text=ourmsg,width=1250,bg="#cc0066",font=("Spectral",15,"bold"))
msg.pack()
button1=Button(frame,text="New Entry",fg="blue",width=30,bd=10,command=callentry)
button2=Button(frame,text="Emergency mode",fg="red",width=30,bd=10,command=callemergency)
button3=Button(frame,text="Normal mode",fg="green",width=30,bd=10,command=callnormal)

button1.pack()
button2.pack()
button3.pack()

master.minsize(1000,500)

mainloop()


import sqlite3
from tkinter import *
from PIL import ImageTk,Image

root=Tk()

frame=Frame(root)
frame.pack()
root.configure(bg="#add5ed")
frame.configure(bg="#add5ed")



L11=Label(frame,text="UNIQUE ID SHOULD CONSIST OF 6 DIGITS",height=5,width=50,fg="black",bg="#add5ed")
L0=Label(frame,text="UNIQUE ID:",height=5,width=15,bg="#add5ed",font=("Spectral",10,"bold"))
L1=Label(frame,text="NAME:",height=5,width=15,bg="#add5ed",font=("Spectral",10,"bold"))
L2=Label(frame,text="ADDRESS:",height=5,width=15,bg="#add5ed",font=("Spectral",10,"bold"))
L3=Label(frame,text="CONTACT NUMBER: ",height=5,width=15,bg="#add5ed",font=("Spectral",10,"bold"))
L4=Label(frame,text="ALLERGIC TO:",height=5,width=15,bg="#add5ed",font=("Spectral",10,"bold"))
L5=Label(frame,text="BLOOD GROUP:",height=5,width=15,bg="#add5ed",font=("Spectral",10,"bold"))
L6=Label(frame,text="BP :",height=5,width=15,bg="#add5ed",font=("Spectral",10,"bold"))
L7=Label(frame,text="MAJOR ILLNESS :",height=5,width=15,bg="#add5ed",font=("Spectral",10,"bold"))
L8=Label(frame,text="MEDICAL HISTORY:",height=5,width=15,bg="#add5ed",font=("Spectral",10,"bold"))

E0=Entry(frame) #id
E1=Entry(frame)  #name
E2=Entry(frame)  #address
E3=Entry(frame)  #contact
E4=Entry(frame)  #allergies
E5=Entry(frame)  #blood group
E6=Entry(frame)  #bp
E7=Entry(frame,width=20)  #major illness
E8=Entry(frame)  #medical history




L11.grid(row=1,column=3)
L0.grid(row=1)

E0.grid(row=1,column=1)
L1.grid(row=2)
E1.grid(row=2,column=1)
L2.grid(row=3)
E2.grid(row=3,column=1)
L3.grid(row=4)
E3.grid(row=4,column=1)
L4.grid(row=5)
E4.grid(row=5,column=1)
L5.grid(row=6)
E5.grid(row=6,column=1)
L6.grid(row=6,column=3)
E6.grid(row=6,column=4)
L7.grid(row=8)
E7.grid(row=8,column=1)
L8.grid(row=8,column=3)
E8.grid(row=8,column=4)


  
def search():
  uni = E0.get()
  name = E1.get()
  add = E2.get()
  cont = E3.get()
  alg = E4.get()
  bld = E5.get()
  bp = E6.get()
  major_ill=E7.get()
  med_hist=E8.get()
  
  id_entered = E0.get()
  id_to_be_checked = int(id_entered)
  conn = sqlite3.connect('data.db')
  c=conn.cursor()
  c.execute('''create table if not exists newTable (uni Integer,name text,address text,cont int,algerdies text,bloodg text,bp text,majorill text,medhist text)''')
  data=c.execute('''select * from newTable''')
  flag=0
  for i in data.fetchall():
      id_in_database = int(i[0])
      if(id_in_database==id_to_be_checked):
          print("Id already exist")
          l=Label(frame,text="Id already Exists",fg="red" )
          l.grid(row=1,column=0)
          flag=1
  if (flag==0):
      c.execute('''insert into newTable  values(%s,'%s','%s','%s','%s','%s','%s','%s','%s')''' %(uni,name,add,cont,alg,bld,bp,major_ill,med_hist))
      conn.commit()
      
  

b1=Button(frame,text="SAVE",bg="green",width=20, height=3,command=search ,font=("bold"))
b1.grid(row=14,column=1)
b1=Button(frame,text="EXIT",bg="#4498c9",width=20,height=3, command=exit ,font=("bold"))
b1.grid(row=14,column=4)



root.minsize(1000,1000)
root.mainloop()

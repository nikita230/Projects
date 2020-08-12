from tkinter import *
import sqlite3 as sqlite3

def search():
    id_entered = E0.get()
    id_to_be_checked = int(id_entered)
    conn = sqlite3.connect('data.db')
    data=conn.execute('''select * from newTable''')
    flag=0
    for j in data:
        id_in_database = int(j[0])
        if(id_in_database==id_to_be_checked):
            flag = 1
            i=j
    if(flag == 1):
        print(i[0]," ",i[1]," ",i[3]," ",i[4]," ",i[5]," ",i[6]," ",i[7])
        uni=Label(frame,text="Unique ID:",font=("Bold",14),bg="#c8bceb")
        uni.grid(row=13,column=0)
        uni1=Label(frame,text=i[0],bg="#c8bceb",font=("Spectral",14))
        uni1.grid(row=13,column=1)
        
        name=Label(frame,text="Name :",font=("Bold",14),bg="#c8bceb")
        name.grid(row=14,column=0)
        name1=Label(frame,text=i[1],bg="#c8bceb",font=("Spectral",14))
        name1.grid(row=14,column=1)
        
        con=Label(frame,text="Contact no :",font=("Bold",14),bg="#c8bceb")
        con.grid(row=15,column=0)
        con1=Label(frame,text=i[3],bg="#c8bceb",font=("Spectral",14))
        con1.grid(row=15,column=1)
        
        alg=Label(frame,text="Alergies ;",font=("Bold",14),bg="#c8bceb")
        alg.grid(row=16,column=0)
        alg1=Label(frame,text=i[4],bg="#c8bceb",font=("Spectral",14))
        alg1.grid(row=16,column=1)

        bld=Label(frame,text="Blood group :",bg="#c8bceb",font=("Bold",14))
        bld.grid(row=17,column=0)
        bld1=Label(frame,text=i[5],bg="#c8bceb",font=("Spectral",14))
        bld1.grid(row=17,column=1)


        bp=Label(frame,text="Blood pressure:",bg="#c8bceb",font=("Bold",14))
        bp.grid(row=18,column=0)
        bp1=Label(frame,text=i[6],bg="#c8bceb",font=("Spectral",14))
        bp1.grid(row=18,column=1)

        maj=Label(frame,text="Major Illness:",bg="#c8bceb",font=("Bold",14))
        maj.grid(row=19,column=0)
        maj1=Label(frame,text=i[7],bg="#c8bceb",font=("Spectral",14))
        maj1.grid(row=19,column=1)
    else :
       not_found=Label(frame,text="Not Found",font=("Bold",14))
       not_found.grid(row=12,column=0)
       
master = Tk()
master.configure(bg="#c8bceb")
frame=Frame(master)
frame.configure(bg="#c8bceb")
frame.pack()
L=Label(frame,text="EMERGENCY",font=("Spectral",15,"bold"),bg="#c8bceb")
L.grid(row=0,column=0)
L0=Label(frame,text="UNIQUE ID:",height=5,width=15,bg="#c8bceb",font=("Spectral",14))
E0=Entry(frame)
L0.grid(row=1,sticky=E)
E0.grid(row=1,column=2)
b1=Button(frame,text="Enter",bg="#c8bceb",width=20,command=search)
b1.grid(row=5,sticky=S)
master.minsize(500,500)
master.mainloop()




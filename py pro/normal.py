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
        #print(i[0]," ",i[1]," ",i[2]," ",i[3]," ",i[4]," ",i[5]," ",i[6]," ",i[7]," " ,i[8])
        name=Label(frame,text="Name :",bg="#aca1cc",font=("Bold",14))
        name.grid(row=11,column=0)
        name1=Label(frame,text=i[1],bg="#aca1cc",font=("Spectral",14))
        name1.grid(row=11,column=1)
        
        add=Label(frame,text="Address",bg="#aca1cc",font=("Bold",14))
        add.grid(row=12,column=0)
        add1=Label(frame,text=i[2],bg="#aca1cc",font=("Spectral",14))
        add1.grid(row=12,column=1)
        
        contact=Label(frame,text="Contact No.:",bg="#aca1cc",font=("Bold",14))
        contact.grid(row=13,column=0)
        contact1=Label(frame,text=i[3],bg="#aca1cc",font=("Spectral",14))
        contact1.grid(row=13,column=1)
        
        alg=Label(frame,text="Alergies :",bg="#aca1cc",font=("Bold",14))
        alg.grid(row=14,column=0)
        alg1=Label(frame,text=i[4],bg="#aca1cc",font=("Spectral",14))
        alg1.grid(row=14,column=1)
        
        bldg=Label(frame,text="Bloodgroup :",bg="#aca1cc",font=("Bold",14))
        bldg.grid(row=15,column=0)
        bldg1=Label(frame,text=i[5],bg="#aca1cc",font=("Spectral",14))
        bldg1.grid(row=15,column=1)

        bp=Label(frame,text="BP :",bg="#aca1cc",font=("Bold",14))
        bp.grid(row=16,column=0)
        bp1=Label(frame,text=i[6],bg="#aca1cc",font=("Spectral",14))
        bp1.grid(row=16,column=1)

        maj=Label(frame,text="Major Illness :", bg="#aca1cc",font=("Bold",14))
        maj.grid(row=17,column=0)
        maj1=Label(frame,text=i[7],bg="#aca1cc",font=("Spectral",14))
        maj1.grid(row=17,column=1)
        
        hist=Label(frame,text="Medical History :", bg="#aca1cc",font=("Bold",14))
        hist.grid(row=18,column=0)
        hist1=Label(frame,text=i[8],bg="#aca1cc",font=("Spectral",14))
        hist1.grid(row=18,column=1)

        
       
    else :
        not_found=Label(frame,text="Not Found",font=("Bold",14))
        not_found.grid(row=12,column=0)




def edit():
    
    data2=E1.get()
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
        data1=i[8]
        data=data1+data2
        conn.execute(''' UPDATE newTable set medhist= ?
                            WHERE uni=?''',(data,id_entered))
        conn.commit()
        
        
      
    
  
       
    

master = Tk()
master.configure(bg="#aca1cc")

frame=Frame(master)
frame.configure(bg="#aca1cc")
frame.pack()



L0=Label(frame,text="UNIQUE ID:",height=5,width=15,bg="#aca1cc",font=("Bold"))
E0=Entry(frame)
L0.grid(row=0,sticky=E)
E0.grid(row=0,column=1)


L1=Label(frame,text="ENTER HISTORY:",height=5,width=15,bg="#aca1cc",font=("Bold"))
E1=Entry(frame)
L1.grid(row=1,sticky=E)
E1.grid(row=1,column=1)




b1=Button(frame,text="GET INFO",bg="#6d6680",width=10,command=search,font=("Bold"))
b1.grid(row=5,column=0)

b2=Button(frame,text="EDIT HISTORY",bg="#6d6680",width=10,command=edit,font=("Bold"))
b2.grid(row=5,column=1)

master.minsize(500,500)
master.mainloop()

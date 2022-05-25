import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import sqlite3 
_u=_p=""
a_a=0
def doon(a,b):
    global _u,_p
    _u=a
    _p=b
    print(_u,_p)
def poon():
    global _u,_p,a_a
    tk5=Tk()
    tk5.geometry("600x500")
    name=StringVar()
    lname=StringVar()
    phone=StringVar()
    user=StringVar()
    password=StringVar()
    
    #หน้าเเก้ไขข้อมูล
    def doom_1():
        global a_a
        print(f"""update doveakaproject set _fname = "{name.get()}", _lname="{lname.get()}",_phone="{phone.get()}",_user="{user.get()}",_password="{password.get()}" where ID="{a_a}" """ )
        conn = sqlite3.connect("project1.db")
        c = conn.cursor()
        c.execute(f"""update doveakaproject set _fname = "{name.get()}", _lname="{lname.get()}",_phone="{phone.get()}",_user="{user.get()}",_password="{password.get()}" where ID="{a_a}" """ )
        conn.commit()
        c.close()
        tk5.destroy() 
        import login
         

    def doom():
        global _u,_p,a_a
        Ibl.place(x=1000,y=0)
        bbu.place(x=1000,y=475)
        Iblr = Label(tk5,image=imge) #สร้าง เลเบล สำหรับเก็บรูป
        Iblr.place(x=0,y=0) #ใช้คำสั่ง pack เพื่อให้ทำหน้าที่จัดวางรูปภาพ กึ่งกลาง 
        entry1 = Entry(tk5,textvariable=name,fg = "#333333",font=('Times',20) ).place(x=106,y=136,width=152,height=42)
        entry2 = Entry(tk5,textvariable=lname,fg = "#333333",font=('Times',20) ).place(x=371,y=136,width=150,height=42)
        entry3 = Entry(tk5,textvariable=phone,fg = "#333333",font =('Times',15) ).place(x=143,y=213,width=146,height=42)
        entry4 = Entry(tk5,textvariable=user,fg = "#333333",font=('Times',13) ).place(x=193,y=372,width=174,height=29)
        x2=Entry(tk5,textvariable=password,fg = "#333333",font=('Times',13) ).place(x=193,y=412,width=174,height=29)
        bbuw=Button(text="ยืนยันข้อมูล",command=doom_1)
        bbuw.place(x=537,y=474)
        conn = sqlite3.connect("project1.db")
        c = conn.cursor()
        data=c.execute(f""" SELECT * FROM doveakaproject WHERE _user=="{_u}" and _password=="{_p}" """ )
        
        for i in data:
            name.set(i[1])
            lname.set(i[2])
            phone.set(i[3])
            user.set(i[4])
            password.set(i[5])
            a_a=i[0]
    ##หน้าเข้าสู่ระบบ##
    # imge = PhotoImage(file="C:\\Users\\taksin\\OneDrive - Khon Kaen University\\Desktop\\python\\pro\\_qqq.png") 
    imge = PhotoImage(file="C:\\Users\\taksin\\OneDrive - Khon Kaen University\\Desktop\\python\\pro\\akadove64.png")
    img = PhotoImage(file="C:\\Users\\taksin\OneDrive - Khon Kaen University\\Desktop\\python\\pro\\_aapp.png")
    Ibl = Label(tk5,image=img)
    Ibl.place(x=0,y=0)
    bbu=Button(text="เเก้ไขข้อมูล",command=doom)
    bbu.place(x=0,y=475)
    tk5.mainloop()
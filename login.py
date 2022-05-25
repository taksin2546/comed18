from logging import root #เรียกใช้ระบบล็อกอิน
import tkinter as tk #
from tkinter import messagebox #เรียกใช้ thinter ของ tk 
import tkinter.font as tkFont
from tkinter import * 
import sqlite3 
tk1=Tk()
tk1.geometry("600x500")
tk1.option_add("*Font","consolas 20")
img = PhotoImage(file="C:\\Users\\taksin\OneDrive - Khon Kaen University\\Desktop\\python\\pro\\_login.png") 
def info(): #สร้างตัวเเปรเป็น x_1 จากนั้น ใช้คำสั่งdestroy เเละimport app2 เข้ามา ก็คือหน้าสร้างบัญชีผู้ใช้
    tk1.destroy() #ลบหน้า tk1 ออก เเล้ว import app2 ขึ้นมาใหม่
    import app2
# CREATE TABLE "doveakaproject" (
# 	"ID"	INTEGER,
# 	"_fname"	TEXT NOT NULL,
# 	"_lname"	TEXT NOT NULL,
# 	"_phone"	TEXT NOT NULL,
# 	"_user"	TEXT NOT NULL,
# 	"_password"	TEXT,
# 	PRIMARY KEY("ID" AUTOINCREMENT)
# );
#หน้าหลัก#
def login(): #
    if user.get() != "" and password.get() != "":
        login1()
    else:
        messagebox.showerror("Error","ไม่พบชื่อ Username ของท่าน \nกรุณากรอก Username และ password ใหม่ \nหากไม่มีบัญชีผู้ใช้งาน กรุณาสมัครบัญชีผู้ใช้งานก่อน")

def login1(): #สร้างตัวเเปรเป็น x_3_ ใช้คำสั่ง command เพราะเป็นตัวเชือม def
    conn = sqlite3.connect("project1.db") #จากนั้น ใช้คำสั่ง conn เพื่อที่จะดึง ข้อมูลจาก db เข้ามาใช้ เเละดึงชื่อไฟล์ ("dove4.db") เข้ามา
    c = conn.cursor() #ใช้ต่อย่อ c = conn.cursor() 
    #ส่วนของการสร้างหน้าล็อคอิน
    a=c.execute('SELECT * FROM doveakaproject') #เเสดงค่าในดาต้าเบส ว่ามีอะไรบ้าง 
    for i in a: #ใช้ลูป for ในการวนอ่านค่าในตัวเเปร เเละโปรเเกรมจะวนอ่านค่าทีละตัวเเล้วเก็บไว้ใน i
        if user.get() == i[4] and password.get() == i[5]: #ใช้คำสั่ง if เพื่อกำหนดให้โปรเเกรมทำงานตามเงื่อนไข x.get() == i[4] and y.get()==i[5]:
            tk1.destroy() #ใช้คำสั่ง destroy 
            import app1 #import app1 เข้ามา
            app1.doon(user.get() , password.get())
            app1.poon()


user=StringVar() 
password=StringVar()
Ibl = Label(tk1,image=img) #สร้าง เลเบล สำหรับเก็บรูป
Ibl.place(x=0,y=0) #ใช้คำสั่ง pack เพื่อให้ทำหน้าที่จัดวางรูปภาพ กึ่งกลาง 
Button(tk1,command=login,text = "เข้าสู่ระบบ",fg = "#5fb878",font = ('JasmineUPC',15) ).place(x=329,y=284,width=120,height=30)
Entry(tk1,fg = "#333333",font=('Times',15),textvariable=user).place(x=250,y=147,width=205,height=38)        
Entry(tk1,fg = "#333333",font=('Times',15),textvariable=password,show="*").place(x=250,y=201,width=205,height=38)
Button(tk1,command=info,text = "สมัครบัญชีผู้ใช้",fg = "#01aaed",font=('JasmineUPC',15) ).place(x=161,y=284,width=120,height=30)

tk1.mainloop()
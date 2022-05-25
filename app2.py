from ast import Str
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import *
import sqlite3

conn = sqlite3.connect("project1.db")
c = conn.cursor()
##หน้าสมัครบัญชีผู้ใช้##
tk2=Tk()
tk2.geometry("600x500")
x=[]
img = PhotoImage(file="C:\\Users\\taksin\\OneDrive - Khon Kaen University\\Desktop\\python\\pro\\_alogin.png") 
name=StringVar()
lname=StringVar()
phone=StringVar()
user=StringVar()
password=StringVar()

def s1():
    def save():
        na = str(name.get()) #กำหนดค่า ชื่อให้เป็น srting
        h = phone.get() #ตัวเเปร
        length = len(h) #เอา len มานับ
        if na.isalpha() == True  and length == 10 \
            and h[:10].isdigit():
            conn = sqlite3.connect("project1.db")
            c = conn.cursor()
            data = (name.get(),lname.get(),phone.get(),user.get(),password.get())
            c.execute('INSERT INTO doveakaproject (_fname,_lname,_phone,_user,_password) VALUES (?,?,?,?,?)',data)
            conn.commit()
            c.close()
            tk2.destroy() #ใช้คำสั่ง destroy 
            import login #import app1 เข้ามา 
        else:
            messagebox.showerror("Error","ข้อมูลของท่านไม่ถูกต้อง \nกรุณาตรวจสอบเเละกรอกข้อมูลใหม่")

    Ibl = Label(tk2,image=img) #สร้าง เลเบล สำหรับเก็บรูป
    Ibl.place(x=0,y=0) #ใช้คำสั่ง pack เพื่อให้ทำหน้าที่จัดวางรูปภาพ กึ่งกลาง 
    entry1 = Entry(tk2,textvariable=name,fg = "#333333",font=('Times',20) ).place(x=106,y=136,width=152,height=42)
    entry2 = Entry(tk2,textvariable=lname,fg = "#333333",font=('Times',20) ).place(x=371,y=136,width=150,height=42)
    entry3 = Entry(tk2,textvariable=phone,fg = "#333333",font =('Times',15) ).place(x=143,y=213,width=146,height=42)

    Button(tk2,command=save,text = "เข้าสู่ระบบ",fg = "#000000",font=('Times',10) ).place(x=400,y=440,width=70,height=35)

    entry4 = Entry(tk2,textvariable=user,fg = "#333333",font=('Times',13) ).place(x=193,y=372,width=174,height=29)
    x2=Entry(tk2,textvariable=password,fg = "#333333",font=('Times',13) ).place(x=193,y=412,width=174,height=29)

    tk2.mainloop()
s1()
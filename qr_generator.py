from tkinter import *
import tkinter as tk
from tkinter.messagebox import askyesno
import pyqrcode
import png
from PIL import Image, ImageTk

root=tk.Tk()
root.title("Qr Code generator")
root.minsize(500,500)
root.iconbitmap("qr-code.ico")
root.configure(bg="#FFFFF0")

title_label=tk.Label(root,text="Welcome to Qr Code Generator!!",bg="#FFFFF0",font=("Arial",20,"bold italic")).pack()

l1=tk.Label(root,text="Enter text or link here",bg="#FFFFF0",font=("Arial",16,"bold italic")).place(x=140,y=50)
b_l1=StringVar()
e1=Entry(root,textvariable=b_l1,justify=LEFT,width=45,bg="white",foreground="black").place(x=120,y=85)
l2=tk.Label(root,text="Name of image:",bg="#FFFFF0",font=('Arial',16,"bold italic")).place(x=10,y=110)
b_l2=StringVar()
e2=Entry(root,textvariable=b_l2,justify=LEFT,width=45,bg="white",foreground="black").place(x=180,y=115)
lb1=tk.Label(root)               
lb1.pack(padx=150,pady=145)

def generate():
    str=b_l1.get()
    q=pyqrcode.create(str)
    st=b_l2.get()
    q.png(st+".png",scale=8)
    p=st+".png"
    img=Image.open(p)
    img=img.resize((200,200))

    img=ImageTk.PhotoImage(img)
    lb1.config(image=img)
    lb1.image=img    
b1=Button(text="GENERATE",command=generate,bg="green",foreground="white").place(x=180,y=455)
def confirm():
    ans=askyesno(title="Confirmation",message="Do you want to Exit!!")
    if ans:
        root.destroy()

root.protocol("WM_DELETE_WINDOW",confirm)

quitbutton=Button(text="EXIT",command=confirm,bg="red",foreground="white").place(x=260,y=455)

root.mainloop()
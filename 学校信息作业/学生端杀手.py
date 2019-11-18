import os
from tkinter import *
from tkinter import messagebox
Window=Tk()
Window.geometry("100x50+540+200")
def task():
    os.system("taskkill -f -im StudentMain.exe")
    messagebox.showinfo(title="提示",message="已关闭学生端")
btn1=Button(Window,text="搞掉学生端",width=15,height=2,command=task)
btn1.grid(row=3,column=0,sticky=W)
Window.mainloop()

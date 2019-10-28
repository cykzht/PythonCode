from tkinter import *
from tkinter import messagebox

#创建窗口
Window=Tk()

#设置窗口的标题
Window.title("你喜欢我吗？")

#窗口大小和位置
Window.geometry("380x400+540+200")

#文字布局和定位
label1=Label(Window,text="Hey,小姐姐",font=('微软雅黑',15),fg='#fe0000')
label2=Label(Window,text="你喜欢我吗？",font=('微软雅黑',15),fg='black')
label1.grid(row=0,column=0,sticky=W)
label2.grid(row=1,column=1,sticky=E)

#加载并显示图片
photo=PhotoImage(file='./love.png')
imageLabel=Label(Window,image=photo)
imageLabel.grid(row=2,columnspan=2)

#按钮和窗口动作方法
def closeWindow():
    messagebox.showinfo(title="警告",message="不许关闭，好好回答")
    return

Window.protocol("WM_DELETE_WINDOW",closeWindow)

def love():
    messagebox.showinfo(title="警告",message="我也是这么想的")
    Window.destroy()
def dislove():
    messagebox.showinfo(title="警告",message="再考虑一下呗")
    return

#按钮布局和显示
btn1=Button(Window,text="喜欢",width=15,height=2,command=love)
btn2=Button(Window,text="不喜欢",command=dislove)
btn1.grid(row=3,column=0,sticky=W)
btn2.grid(row=3,column=1,sticky=E)

#显示窗口
Window.mainloop()

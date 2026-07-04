import tkinter as tk
from tkinter.ttk import Combobox
a1=tk.Tk()
a1.title('小王')
a1.geometry('500x500+400+200')
a1.resizable(False,False)
#设置窗口图标
a1.iconbitmap('logo.ico')

def t():
  t1=tk.Toplevel()
  t1.title('小王')
  t1.geometry('300x300+400+200')
  t1.resizable(False,False)
  #设置窗口图标
  t1.iconbitmap('logo.ico')
  #设置顶层窗口焦点
  t1.focus_set()
  tk.Label(t1,text='城市:',font=('楷体',16)).grid(row=1,column=1)
  tk.Label(t1,text='性别:',font=('楷体',16)).grid(row=2,column=1)
  t2=tk.StringVar(value='北京')
  s2=tk.StringVar(value='男')
  t3=['北京','上海','深圳']
  #创建下拉列表(组合框)
  t4=Combobox(t1,state='readonly',width=10,textvariable=t2,values=t3,font=('楷体',16))
  t4.grid(row=1,column=2)
  #创建单选框
  tk.Radiobutton(t1,font=('楷体',16),text='男',variable=s2,value='男').place(x=80,y=30)
  tk.Radiobutton(t1,font=('楷体',16),text='女',variable=s2,value='女').place(x=130,y=30)
  def tj():
    print(t2.get())
    print(s2.get())
  tk.Button(t1,text='提交',command=tj).place(x=200,y=200)
#创建主菜单
cai=tk.Menu(a1)
#创建下级菜单
xia=tk.Menu(cai,tearoff=0)
#设置下级菜单
xia.add_command(label='添加',command=t)

#设置菜单名
#绑定到主菜单
cai.add_cascade(label='员工',menu=xia)

#开启菜单栏
a1.config(menu=cai)
#结束语句
a1.mainloop()
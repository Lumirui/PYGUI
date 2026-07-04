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
  tk.Label(t1,text='城市:',font=('楷体',16)).grid(row=1,column=1)
  t2=tk.StringVar()
  t3=['北京','上海','深圳']
  #创建下拉列表(组合框)
  t4=Combobox(t1,state='readonly',width=10,textvariable=t2,values=t3,font=('楷体',16))
  t4.grid(row=1,column=2)
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
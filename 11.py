import tkinter as tk
from tkinter import messagebox
a1=tk.Tk()
a1.title('登录页')
a1.geometry('500x400')
a1.resizable(False,False)
#设置窗口图标
a1.iconbitmap('logo.ico')

tk.Label(a1,text='账号:',font=('黑体',26)).place(x=50,y=100)
tk.Label(a1,text='密码:',font=('黑体',26)).place(x=50,y=180)
#创建字符串变量
s1=tk.StringVar()
#预设文本,不是placeholder
s1.set('请输入账号')
s2=tk.StringVar()
s2.set('请输入密码')

#输入框组件
tk.Entry(a1,textvariable=s1,width=15,font=('黑体',26)).place(x=150,y=100)
tk.Entry(a1,textvariable=s2,width=15,font=('黑体',26)).place(x=150,y=180)

def guan():
  d1=messagebox.askokcancel('是否关闭','确定关闭吗')
  if d1:
    a1.destroy()
  else:
    pass
def dl():
  # print('小王')
  #字符串变量获取
  print(s1.get())
  print(s2.get())
  if s1.get()!='123' or s2.get()!='123':
    print('账号或密码错误')
    #messagebox.showerror('错误','账号或密码错误')
    #messagebox.showinfo('错误','账号或密码错误')
    #messagebox.showwarning('错误','账号或密码错误')
    d1=messagebox.askokcancel('错误','账号密码错误')
    if d1:
      print('确定')
    else:
      print('取消')
  else:
    messagebox.showinfo('成功','登录成功')
def zc():
  a2=tk.Toplevel()
  a2.title('注册页')
  a2.geometry('300x300')
  a2.resizable(False,False)
  #设置窗口图标
  a2.iconbitmap('logo.ico')
  tk.Label(a2,text='账号:',font=('楷体',16)).grid(row=1,column=1)
  tk.Label(a2,text='密码:',font=('楷体',16)).grid(row=2,column=1)
  tk.Entry(a2,width=15,font=('黑体',26)).grid(row=1,column=2)
  tk.Entry(a2,width=15,font=('黑体',26)).grid(row=2,column=2)
  tk.Button(a2,command='',text='注册',font=('楷体',20)).place(x=100,y=100)
tk.Button(a1,command=dl,text='登录',font=('黑体',26),width=10).place(x=80,y=280)
tk.Button(a1,command=zc,text='注册',font=('黑体',26),width=10).place(x=300,y=280)



a1.protocol('WM_DELETE_WINDOW',guan)


#结束语句
a1.mainloop()
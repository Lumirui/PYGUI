import tkinter as tk
from tkinter import messagebox
a1=tk.Tk()
a1.title('登录页')
#获取用户分辨率,这样设置更合理
a2=a1.maxsize()
print(a2)
k,g=a2
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
tk.Button(a1,text='登录',command=dl,font=('黑体',26),width=10).place(x=150,y=280)
#结束语句
a1.mainloop()
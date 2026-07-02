import tkinter as tk
a1=tk.Tk()
a1.title('登录页')
#获取用户分辨率,这样设置更合理
a2=a1.maxsize()
print(a2)
k,g=a2
a1.geometry(f'{int(k/2)}x{int(g/2)}')
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
#结束语句
a1.mainloop()
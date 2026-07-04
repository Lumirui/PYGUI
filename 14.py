import tkinter as tk
a1=tk.Tk()
a1.title('小王')
a1.geometry('500x500+400+200')
a1.resizable(False,False)
#设置窗口图标
a1.iconbitmap('logo.ico')
#创建主菜单
cai=tk.Menu(a1)
#创建下级菜单
xia=tk.Menu(cai,tearoff=0)
#设置下级菜单
xia.add_command(label='添加',command='')

#设置菜单名
#绑定到主菜单
cai.add_cascade(label='员工',menu=xia)

#开启菜单栏
a1.config(menu=cai)


#结束语句
a1.mainloop()
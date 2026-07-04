import tkinter as tk
a1=tk.Tk()
a1.title('小王')
a1.geometry('500x500+400+200')
a1.resizable(False,False)
#设置窗口图标
a1.iconbitmap('logo.ico')
#创建主菜单
cai=tk.Menu(a1)
#设置菜单名
cai.add_cascade(label='员工1')
cai.add_cascade(label='员工2')
#开启菜单栏
a1.config(menu=cai)
#结束语句
a1.mainloop()
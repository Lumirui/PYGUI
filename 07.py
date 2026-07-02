import tkinter as tk
a1=tk.Tk()
a1.title('小王')
#获取用户分辨率,这样设置更合理
a2=a1.maxsize()
print(a2)
k,g=a2
a1.geometry(f'{int(k/2)}x{int(g/2)}')
a1.resizable(False,False)
#设置窗口图标
a1.iconbitmap('logo.ico')

#标签组件
a2=tk.Label(a1,text='小王',font=('黑体',20),fg='blue',bg='brown').grid(row=1,column=1)
#填充布局
# a2.pack()
#自定义布局 place()
# a2.place(x=100,y=100) #不超过窗口范围
#网格布局
# a2.grid(row=1,column=1)
#结束语句
a1.mainloop()
import tkinter as tk
a1=tk.Tk()
a1.title('小王')
#获取用户分辨率,这样设置更合理
a2=a1.maxsize()
print(a2)
k,g=a2
a1.geometry(f'{int(k/2)}x{int(g/2)}')
a1.resizable(False,False)
#结束语句
a1.mainloop()
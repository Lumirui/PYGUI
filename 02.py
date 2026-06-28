import tkinter as tk

a1=tk.Tk()
a1.title('小王')
#获取用户分辨率
a2=a1.maxsize()
print(a2)
k,g=a2
a1.geometry(f'{int(k/2)}x{int(g/2)}')
a1.geometry('400x500+200+300')
a1.mainloop()
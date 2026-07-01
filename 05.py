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

def close():
  print('关')
  #销毁窗口/组件
  a1.destroy()
#设置窗口制定
a1.attributes('-topmost',True)
#设置窗口关闭时执行的参数
a1.protocol('WM_DELETE_WINDOW',close)

#结束语句
a1.mainloop()
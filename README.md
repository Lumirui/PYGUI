# Python Tkinter 知识点总结

> 基于 01.py ~ 17.py 的完整学习记录，涵盖 Tkinter GUI 开发的核心知识点。

---

## 目录

1. [创建窗口与主循环](#1-创建窗口与主循环)
2. [窗口大小与屏幕适配](#2-窗口大小与屏幕适配)
3. [窗口锁定与图标](#3-窗口锁定与图标)
4. [窗口背景与透明度](#4-窗口背景与透明度)
5. [窗口置顶与关闭协议](#5-窗口置顶与关闭协议)
6. [Label 标签组件](#6-label-标签组件)
7. [三种布局管理器](#7-三种布局管理器)
8. [Entry 输入框与 StringVar](#8-entry-输入框与-stringvar)
9. [Button 按钮与事件回调](#9-button-按钮与事件回调)
10. [MessageBox 消息弹窗](#10-messagebox-消息弹窗)
11. [Toplevel 子窗口](#11-toplevel-子窗口)
12. [字典存储与登录注册系统](#12-字典存储与登录注册系统)
13. [Menu 菜单栏](#13-menu-菜单栏)
14. [子菜单与命令绑定](#14-子菜单与命令绑定)
15. [Combobox 下拉列表](#15-combobox-下拉列表)
16. [Radiobutton 单选框](#16-radiobutton-单选框)
17. [Checkbutton 多选框与 Listbox 列表框](#17-checkbutton-多选框与-listbox-列表框)
18. [完整项目：员工管理系统](#18-完整项目员工管理系统)

---

## 1. 创建窗口与主循环

**对应文件：01.py**

```python
import tkinter as tk          # 导入 tkinter 并简写为 tk
window = tk.Tk()              # 创建主窗口（变量名可自定义）
window.title('窗口标题')        # 设置窗口标题（默认为 "tk"）
window.mainloop()             # 窗口主循环（必须放在最后）
```

| 函数 | 说明 |
|------|------|
| `tk.Tk()` | 创建主窗口实例 |
| `.title(str)` | 设置窗口标题 |
| `.mainloop()` | 进入事件主循环，保持窗口显示 |

---

## 2. 窗口大小与屏幕适配

**对应文件：02.py**

### 固定大小

```python
a1.geometry('400x500')            # 宽400，高500（注意：乘号是小写字母 x）
a1.geometry('400x500+200+300')    # 宽400，高500，起始位置 (200, 300)
```

### 获取屏幕分辨率并自适应

```python
a2 = a1.maxsize()                 # 获取屏幕最大分辨率，返回 (宽, 高)
print(a2)                         # 例如：(1920, 1080)

k, g = a2                         # 元组解包：k=宽，g=高
a1.geometry(f'{int(k/2)}x{int(g/2)}')  # 窗口设为屏幕一半大小
```

| 函数 | 说明 |
|------|------|
| `.geometry('WxH+X+Y')` | 设置窗口大小和位置 |
| `.maxsize()` | 获取屏幕最大分辨率，返回 `(宽度, 高度)` |

---

## 3. 窗口锁定与图标

**对应文件：03.py**

```python
a1.resizable(False, False)        # 禁止用户拖拽改变窗口大小
a1.iconbitmap('logo.ico')         # 设置窗口图标（建议使用相对路径）
```

| 函数 | 说明 |
|------|------|
| `.resizable(width, height)` | `True` 允许拖拽，`False` 锁定大小 |
| `.iconbitmap('路径.ico')` | 设置窗口左上角图标（仅支持 `.ico` 格式） |

---

## 4. 窗口背景与透明度

**对应文件：04.py**

```python
a1.config(bg='blue')              # 设置背景颜色（支持颜色名或十六进制编码）
a1.attributes('-alpha', 0.5)      # 设置窗口透明度（0.0 ~ 1.0，1为完全不透明）
```

| 函数 | 说明 |
|------|------|
| `.config(bg='颜色')` | 设置背景颜色 |
| `.attributes('-alpha', 值)` | 设置窗口透明度，范围 `0.0`（全透明）~ `1.0`（不透明） |

> **颜色选择工具：** https://tools.jb51.net/static/colorpicker/

---

## 5. 窗口置顶与关闭协议

**对应文件：05.py**

```python
def close():
    print('关')
    a1.destroy()                   # 销毁窗口/组件

a1.attributes('-topmost', True)    # 窗口置顶（始终在最前）
a1.protocol('WM_DELETE_WINDOW', close)  # 点击关闭按钮时执行 close 函数
```

| 函数 | 说明 |
|------|------|
| `.attributes('-topmost', bool)` | 窗口是否置顶 |
| `.protocol('WM_DELETE_WINDOW', func)` | 拦截窗口关闭事件，执行自定义函数 |
| `.destroy()` | 销毁窗口或组件 |

---

## 6. Label 标签组件

**对应文件：06.py**

```python
a2 = tk.Label(
    a1,                    # 父容器
    text='小王',            # 显示文本
    font=('黑体', 20),      # 字体：(字体名, 字号)
    fg='blue',             # 前景色（文字颜色）
    bg='brown'             # 背景色
)
a2.pack()                  # 使用 pack 布局放置标签
```

| 参数 | 说明 |
|------|------|
| `text` | 显示的文本内容 |
| `font` | 字体设置，格式 `(字体名, 字号)` |
| `fg` / `foreground` | 文字颜色 |
| `bg` / `background` | 背景颜色 |

---

## 7. 三种布局管理器

**对应文件：07.py**

Tkinter 提供三种布局方式，**不能混用**：

### 7.1 pack() — 填充布局

```python
a2.pack()                  # 自动从上到下、居中排列
```

### 7.2 place() — 绝对定位布局

```python
a2.place(x=100, y=100)     # 精确指定坐标（不能超出窗口范围）
```

### 7.3 grid() — 网格布局

```python
a2.grid(row=1, column=1)   # 按行/列放置，行列从0开始
```

| 布局方式 | 特点 | 适用场景 |
|----------|------|----------|
| `pack()` | 自动排列，简单快速 | 简单纵向/横向排列 |
| `place()` | 精确像素定位 | 需要精确控制位置 |
| `grid()` | 表格形式排列 | 表单、规则布局 |

> **注意：** 同一个容器内不能混用 pack / place / grid！

---

## 8. Entry 输入框与 StringVar

**对应文件：08.py**

```python
# 创建字符串变量
s1 = tk.StringVar()
s1.set('请输入账号')        # 预设文本（不是 placeholder，需要手动清除）

# 创建输入框
tk.Entry(
    a1,                     # 父容器
    textvariable=s1,        # 绑定的字符串变量
    width=15,               # 宽度（字符数）
    font=('黑体', 26)
).place(x=150, y=100)
```

| 组件/类 | 说明 |
|---------|------|
| `tk.StringVar()` | 创建 Tkinter 字符串变量 |
| `.set(value)` | 设置变量值（同时更新关联组件） |
| `tk.Entry()` | 单行文本输入框 |
| `textvariable` | 将 Entry 与 StringVar 双向绑定 |

---

## 9. Button 按钮与事件回调

**对应文件：09.py**

```python
def dl():
    print(s1.get())        # 通过 .get() 获取 StringVar 的值
    print(s2.get())

tk.Button(
    a1,
    text='登录',             # 按钮文字
    command=dl,              # 点击时执行的函数（不要加括号！）
    font=('黑体', 26),
    width=10                 # 按钮宽度
).place(x=150, y=280)
```

| 参数 | 说明 |
|------|------|
| `text` | 按钮显示文字 |
| `command` | 点击回调函数（传函数引用，不传调用结果） |
| `width` | 按钮宽度 |
| `.get()` | 从 StringVar 获取当前值 |

---

## 10. MessageBox 消息弹窗

**对应文件：10.py**

```python
from tkinter import messagebox

# 四种弹窗类型
messagebox.showerror('错误', '账号或密码错误')       # 错误图标
messagebox.showinfo('成功', '登录成功')              # 信息图标
messagebox.showwarning('警告', '请输入完整信息')     # 警告图标

# 带返回值的确认弹窗
d1 = messagebox.askokcancel('确认', '账号密码错误，是否继续？')
if d1:
    print('用户点击了确定')    # 返回 True
else:
    print('用户点击了取消')    # 返回 False
```

| 函数 | 图标 | 返回值 |
|------|------|--------|
| `showerror(title, msg)` | ❌ 错误 | 无 |
| `showinfo(title, msg)` | ℹ️ 信息 | 无 |
| `showwarning(title, msg)` | ⚠️ 警告 | 无 |
| `askokcancel(title, msg)` | ❓ 确认 | `True`（确定） / `False`（取消） |

---

## 11. Toplevel 子窗口

**对应文件：11.py**

```python
def guan():
    d1 = messagebox.askokcancel('是否关闭', '确定关闭吗')
    if d1:
        a1.destroy()         # 关闭主窗口

def zc():
    a2 = tk.Toplevel()       # 创建子窗口（独立于主窗口）
    a2.title('注册页')
    a2.geometry('300x300')
    a2.resizable(False, False)
    a2.iconbitmap('logo.ico')
    # ... 在子窗口中添加组件 ...

a1.protocol('WM_DELETE_WINDOW', guan)   # 点击X时触发 guan 函数
```

| 函数/属性 | 说明 |
|-----------|------|
| `tk.Toplevel()` | 创建子窗口（可多个，独立于主窗口） |
| `a1.protocol('WM_DELETE_WINDOW', func)` | 拦截关闭按钮，执行自定义操作 |
| `a1.destroy()` | 销毁窗口 |

---

## 12. 字典存储与登录注册系统

**对应文件：12.py**

```python
hao = {}                     # 用字典存储账号信息：{账号: 密码}

def zc2():
    global hao               # 声明使用全局变量 hao
    if s3.get() not in hao:
        hao[s3.get()] = s4.get()    # 存入字典
        messagebox.showinfo('成功', '注册成功')
        a2.destroy()         # 注册成功后关闭注册窗口
    else:
        messagebox.showerror('错误', '账号已存在')

def dl():
    if s1.get() in hao:                     # 检查账号是否存在
        if s2.get() == hao[s1.get()]:       # 验证密码
            messagebox.showinfo('成功', '登录成功')
        else:
            messagebox.showerror('错误', '密码不正确')
    else:
        messagebox.showerror('错误', '账号不存在')
```

| 知识点 | 说明 |
|--------|------|
| `global` | 在函数内修改全局变量时必须声明 |
| `key in dict` | 检查字典中是否存在某个键 |
| `dict[key] = value` | 向字典添加/修改键值对 |
| `dict[key]` | 通过键获取值 |

---

## 13. Menu 菜单栏

**对应文件：13.py**

```python
cai = tk.Menu(a1)                  # 创建主菜单（绑定到窗口）
cai.add_cascade(label='员工1')      # 添加顶级菜单项
cai.add_cascade(label='员工2')
a1.config(menu=cai)                # 将菜单配置到窗口
```

| 函数 | 说明 |
|------|------|
| `tk.Menu(parent)` | 创建菜单对象 |
| `.add_cascade(label='名称')` | 添加菜单项 |
| `.config(menu=菜单对象)` | 将菜单挂载到窗口 |

---

## 14. 子菜单与命令绑定

**对应文件：14.py**

```python
# 创建主菜单
cai = tk.Menu(a1)

# 创建下级菜单（tearoff=0 禁止菜单被拖出）
xia = tk.Menu(cai, tearoff=0)

# 向下级菜单添加命令项
xia.add_command(label='添加', command='')     # command 绑定点击事件

# 将下级菜单绑定到主菜单
cai.add_cascade(label='员工', menu=xia)

# 开启菜单栏
a1.config(menu=cai)
```

| 参数/函数 | 说明 |
|-----------|------|
| `tearoff=0` | 禁止菜单被拖出成独立窗口（推荐设置） |
| `.add_command(label, command)` | 添加可点击的菜单命令项 |
| `cai.add_cascade(label, menu=子菜单)` | 将子菜单绑定到父菜单项 |

---

## 15. Combobox 下拉列表

**对应文件：15.py**

```python
from tkinter.ttk import Combobox

t2 = tk.StringVar()
t3 = ['北京', '上海', '深圳']       # 下拉选项列表

t4 = Combobox(
    t1,
    state='readonly',           # 只读模式（禁止用户输入）
    width=10,
    textvariable=t2,            # 绑定变量
    values=t3,                  # 下拉选项
    font=('楷体', 16)
)
t4.grid(row=1, column=2)
```

| 参数 | 说明 |
|------|------|
| `state='readonly'` | 只读模式，用户只能选择不能输入 |
| `values` | 下拉列表的选项（列表类型） |
| `textvariable` | 绑定 StringVar，获取选中值 |

> **导入注意：** `Combobox` 来自 `tkinter.ttk`，不是 `tkinter`！

---

## 16. Radiobutton 单选框

**对应文件：16.py**

```python
s2 = tk.StringVar(value='男')     # 设置默认选中值

tk.Radiobutton(t1, font=('楷体', 16),
    text='男',                     # 显示文字
    variable=s2,                   # 绑定到同一个变量 → 互斥
    value='男'                     # 选中时变量的值
).place(x=80, y=30)

tk.Radiobutton(t1, font=('楷体', 16),
    text='女',
    variable=s2,                   # 同一个变量，实现互斥
    value='女'
).place(x=130, y=30)

# 获取选中值
print(s2.get())                    # 返回 '男' 或 '女'
```

| 参数 | 说明 |
|------|------|
| `variable` | 绑定的 StringVar，**同一组单选框必须绑定同一个变量** |
| `value` | 选中时写入 variable 的值 |
| `text` | 单选框旁显示的文字 |
| `StringVar(value='默认值')` | 创建时直接设置默认值 |

> **关键：** 同一组 Radiobutton 绑定同一个 `variable`，不同 `value`，自动实现互斥选择。

---

## 17. Checkbutton 多选框与 Listbox 列表框

**对应文件：17.py**

### 17.1 Checkbutton 多选框

```python
# 使用 IntVar（整数变量）—— 0=未选中，1=选中
s3 = tk.IntVar()
s4 = tk.IntVar()

tk.Checkbutton(t1,
    text='跑步',
    variable=s3,
    onvalue=1,       # 选中时变量的值
    offvalue=0       # 未选中时变量的值
).place(x=80, y=57)

tk.Checkbutton(t1,
    text='游泳',
    variable=s4,
    onvalue=1,
    offvalue=0
).place(x=130, y=57)

# 判断是否选中
if s3.get() == 1:
    print('跑步被选中')
```

| 参数 | 说明 |
|------|------|
| `variable` | 绑定 IntVar |
| `onvalue` | 选中时写入的值 |
| `offvalue` | 取消时写入的值 |
| `tk.IntVar()` | 整数变量（适合多选框的 0/1 状态） |

### 17.2 Listbox 列表框

```python
from tkinter import END

lb = tk.Listbox(a1,
    font=('楷体', 16),
    width=40,          # 宽度（字符数）
    height=20          # 高度（行数）
)
lb.place(x=4, y=30)

# 插入数据
lb.insert(END, '要插入的内容')     # END 表示在末尾追加
```

| 参数/常量 | 说明 |
|-----------|------|
| `width` | 列表框宽度（字符数） |
| `height` | 列表框高度（可见行数） |
| `.insert(END, item)` | 在末尾插入一项 |
| `END` | tkinter 常量，表示末尾位置 |

---

## 18. 完整项目：员工管理系统

**对应文件：17.py（最终版本）**

这是 01~17 所有知识点的综合应用，实现了一个带菜单的简易员工信息管理系统：

```
┌──────────────────────────────────────────┐
│  菜单栏：员工 → 添加                       │
├──────────────────────────────────────────┤
│                                          │
│  员工列表（Listbox）                       │
│  ┌────────────────────────────────────┐  │
│  │ 员工1                               │  │
│  │ 员工2                               │  │
│  │ ...                                 │  │
│  └────────────────────────────────────┘  │
│                                          │
│  点击"添加"→弹出子窗口：                    │
│  ┌──────────────────────────────┐        │
│  │  城市: [北京 ▼]  (Combobox)  │        │
│  │  性别: ○男 ○女  (Radiobutton)│        │
│  │  爱好: ☐跑步 ☐游泳 (Checkbutton)│     │
│  │  [提交] (Button)              │        │
│  └──────────────────────────────┘        │
└──────────────────────────────────────────┘
```

---

## 附录：常用组件速查表

| 组件 | 来源 | 用途 |
|------|------|------|
| `tk.Tk()` | tkinter | 主窗口 |
| `tk.Toplevel()` | tkinter | 子窗口 |
| `tk.Label()` | tkinter | 文本标签 |
| `tk.Entry()` | tkinter | 单行输入框 |
| `tk.Button()` | tkinter | 按钮 |
| `tk.Menu()` | tkinter | 菜单栏 |
| `tk.Radiobutton()` | tkinter | 单选框 |
| `tk.Checkbutton()` | tkinter | 多选框 |
| `tk.Listbox()` | tkinter | 列表框 |
| `Combobox()` | tkinter.ttk | 下拉列表 |
| `messagebox` | tkinter | 消息弹窗 |
| `tk.StringVar()` | tkinter | 字符串变量 |
| `tk.IntVar()` | tkinter | 整数变量 |

## 附录：通用窗口配置速查

| 函数 | 说明 |
|------|------|
| `.title(str)` | 窗口标题 |
| `.geometry('WxH+X+Y')` | 窗口大小和位置 |
| `.maxsize()` | 获取屏幕分辨率 |
| `.resizable(x, y)` | 是否可拖拽调整大小 |
| `.iconbitmap('*.ico')` | 窗口图标 |
| `.config(bg='color')` | 背景颜色 |
| `.attributes('-alpha', 0.5)` | 透明度 |
| `.attributes('-topmost', True)` | 窗口置顶 |
| `.protocol('WM_DELETE_WINDOW', func)` | 关闭窗口回调 |
| `.destroy()` | 销毁窗口 |
| `.mainloop()` | 主事件循环 |

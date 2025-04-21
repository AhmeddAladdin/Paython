"""
========================================
-----> intro. to GUI with Tkinter <-----
========================================
"""
# 1.main window
from tkinter import *
x = Tk()
x.mainloop()

# =======================================

# 2.window size (width, height, left, down)
from tkinter import *
y = Tk()
y.geometry('500x600+500+100')
y.mainloop()

# ========================================

# 3.block user to control the size
from tkinter import *
a = Tk()
a.geometry('500x600+500+100')
a.resizable(False, True)
a.mainloop()

# =========================================

# 4.Name the window
from tkinter import *
z = Tk()
z.title('Aladdin')
z.mainloop()

# ==========================================

# 5.change background color
from tkinter import *
x = Tk()
x.config(background='light blue')
x.mainloop()

# ==========================================

# 6.change window's icon
from tkinter import *
x = Tk()
x.iconbitmap(r'D:\Python\files')
x.mainloop()

# ==========================================

# 7.max & min size
from tkinter import *
x = Tk()
x.minsize(300, 300)
x.maxsize(600,600)
x.mainloop()

# ==========================================

# 8.max & min size
from tkinter import *
x = Tk()
x.minsize(300, 300)
x.maxsize(600,600)
x.mainloop()

# ==========================================

# 9.frames
from tkinter import *
App = Tk()
App.geometry('800x500')
App.minsize(800,500)

frm1 = Frame(width=200, height=499, bg='gray')
frm1.place(x=1, y=1)

App.mainloop()

# ==========================================

# 10.buttons
from tkinter import *
App = Tk()
App.geometry('800x500')
App.minsize(800,500)

frm1 = Frame(width=200, height=499, bg='gray')
frm1.place(x=1, y=1)

btn1 = Button(frm1, text='Click1', bg='black', fg='white', cursor="arrow")
'''
There are about 20 cursors that can be found in Tkinter:
arrow, circle, clock, cross, dotbox, exchange, fleur, heart,
man, mouse, pirate, plus, shuttle, sizing, spider, spraycan,
star, target, tcross, trek.
'''
btn1.place(x=10, y=10)


App.mainloop()

# ==========================================

# 11.labels
from tkinter import *
App = Tk()
App.geometry('800x500')
App.minsize(800,500)

frm1 = Frame(width=200, height=499, bg='gray')
frm1.place(x=1, y=1)

lbl1 = Label(frm1, text='This is a button', fg='red', bg='gray')
lbl1.place(x=10, y=30)
App.mainloop()
# ==========================================

# 12.Entry
from tkinter import *
App = Tk()
App.geometry('800x500')
App.minsize(800,500)

frm1 = Frame(width=200, height=499, bg='gray')
frm1.place(x=1, y=1)


ent1 = Entry(frm1)
ent1.place(x=10, y=65)

ent2 = Entry(frm1, justify='center', bg='light blue', fg='blue', font=10)
ent2.place(x=10, y=105)

App.mainloop()

# ==========================================

# 13.combobox
from tkinter import *
from tkinter import ttk

App = Tk()

App.geometry('800x500')

cmbo1 = ttk.Combobox(App, values=["Male", "Female"], state='readonly')
cmbo1.place(x=10, y=10)

cmbo2 = ttk.Combobox(App, values=[
    'Cairo', "Mansoura", "Giza", "Alex", 'Port-Said'
], state='readonly')
cmbo2.place(x=10, y=50)

App.mainloop()

# ==========================================

# 14.ListBox
from tkinter import *

App = Tk()

App.geometry('800x500')

lst1 = Listbox(App)
lst1.insert(0, 'one')
lst1.insert(1, 'two')
lst1.insert(2, 'three')
lst1.insert(3, 'four')
lst1.place(x=10, y=10)

App.mainloop()

# ==========================================

# 15.Radiobutton
from tkinter import *
from tkinter import ttk

App = Tk()

App.geometry('800x500')

R_btn1 = ttk.Radiobutton(App, text='Male', value=1)
R_btn2 = ttk.Radiobutton(App, text='Female', value=2)

R_btn1.pack()
R_btn2.pack()

App.mainloop()

# ==========================================

# 16.CheckButton
from tkinter import *

App = Tk()

App.geometry('800x500')

chk1 = Checkbutton(App, text='Sports')
chk2 = Checkbutton(App, text='Drawing')
chk3 = Checkbutton(App, text='Graphic')
chk4 = Checkbutton(App, text='Singing')
chk5 = Checkbutton(App, text='Video Games')

chk1.place(x=10, y=10)
chk2.place(x=10, y=30)
chk3.place(x=10, y=50)
chk4.place(x=10, y=70)
chk5.place(x=10, y=90)

App.mainloop()

# ==========================================

# 17.Menu Button
from tkinter import *

App = Tk()

App.geometry('800x500')

mBtn = Menubutton(App, text='language', relief='groove')
mBtn.pack()

mnu = Menu(mBtn)
mBtn['menu'] = mnu

mnu.add_checkbutton(label='python')
mnu.add_checkbutton(label='C++')
mnu.add_checkbutton(label='Java')


App.mainloop()

# ==========================================

# 18.Menu Bar
from tkinter import *

App = Tk()

App.geometry('800x500')

mnuBar = Menu(App)
mnu = Menu(mnuBar, tearoff=0)

mnu.add_command(label='New file')
mnu.add_command(label='Open file')
mnu.add_command(label='New')
mnu.add_separator()
mnu.add_command(label='Save')
mnu.add_command(label='Save as')
mnu.add_separator()
mnu.add_command(label='Exit', command=App.quit)

mnuBar.add_cascade(label='File1', menu=mnu)

App.config(menu=mnuBar)

App.mainloop()

# ==========================================

# 19.Scale
from tkinter import *

App = Tk()

App.geometry('800x500')

scl1 = Scale(App, from_=1, to=100, orient="horizontal")
scl1.pack()

scl2 = Scale(App, from_=1, to=100, orient="vertical")
scl2.pack()

App.mainloop()

# ==========================================

# 20.Scroll bar
from tkinter import *

App = Tk()

App.geometry('800x500')

scr1 = Scrollbar(App, orient="vertical")
scr1.pack(side='right', fill='y')

scr2 = Scrollbar(App, orient="horizontal")
scr2.pack(side='bottom', fill='x')

App.mainloop()

# ==========================================

# 21.Notebook
from tkinter import *
from tkinter import ttk

App = Tk()

App.geometry('800x500')

ntbk = ttk.Notebook(App)
ntbk.pack()

f1 = Frame(ntbk, width=800, height=100, bg='silver')
ntbk.add(f1, text="Home")
btn = Button(f1, text='Hello')
btn.place(x=10, y=10)

f2 = Frame(ntbk, width=800, height=100, bg='silver')
ntbk.add(f2, text="Insert")


App.mainloop()

# ==========================================

# 22.SpinBox
from tkinter import *

App = Tk()

App.geometry('800x500')

spnBx = Spinbox(App, from_=1, to=100)
spnBx.pack()

App.mainloop()

# ==========================================

# 23.Button Image
from tkinter import *

App = Tk()

App.geometry('800x500')

photo = PhotoImage(file=r'D:\Python\files\Save-Button.png')
resize = photo.subsample(100, 100)

btn = Button(App, text='Save ', image=resize, compound="right")
btn.place(x=10, y=10)

App.mainloop()

# ==========================================

# 24.First Example with Tkinter ==>

# ==========================================

# 25.Text Box
from tkinter import *

App = Tk()

App.geometry('800x500')

txt = Text(App, width=50, height=5)
txt.pack()

App.mainloop()

# ==========================================

# 26.Message Box
from tkinter import *
from tkinter import messagebox

App = Tk()

App.geometry('800x500')


def message():
    messagebox.showinfo('Information', 'Hello to my program my name is Ahmed Alaa')


'''showinfo, showwarning, showerror, askquestion, askokcancel, ...'''

btn1 = Button(App, text='info.', command=message)
btn1.pack()

App.mainloop()

# ==========================================

# The END الحمد لله

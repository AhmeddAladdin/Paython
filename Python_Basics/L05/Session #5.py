"""
========================================
-----> intro. to GUI with Tkinter <-----
========================================
"""

from tkinter import *
from tkinter import ttk

myApp = Tk()
myApp.geometry('800x500')

# List Box
lst1 = Listbox(myApp)
lst1.insert(0, 'Apple')
lst1.insert(0, 'Bread')
lst1.insert(0, 'Milk')
lst1.insert(0, 'Cheese')
lst1.insert(0, 'Meat')
lst1.place(x=20, y=30)

# Radiobutton
RBtn1 = ttk.Radiobutton(myApp, text='Male', value=0)
RBtn2 = ttk.Radiobutton(myApp, text='Female', value=1)
RBtn1.pack()
RBtn2.pack()

# CheckButton
chk1 = Checkbutton(myApp, text='Sports')
chk2 = Checkbutton(myApp, text='Drawing')
chk3 = Checkbutton(myApp, text='Graphic')
chk4 = Checkbutton(myApp, text='Singing')
chk5 = Checkbutton(myApp, text='Video Games')
chk1.place(x=10, y=200)
chk2.place(x=10, y=220)
chk3.place(x=10, y=240)
chk4.place(x=10, y=260)
chk5.place(x=10, y=280)

# Menubutton
mBtn = Menubutton(myApp, text='language', relief='groove')
mBtn.pack()
mnu = Menu(mBtn, tearoff=0)
mBtn['menu'] = mnu
mnu.add_checkbutton(label='python')
mnu.add_checkbutton(label='C++')
mnu.add_checkbutton(label='Java')

# Menu Bar
mnuBar = Menu(myApp)
mnu1 = Menu(mnuBar, tearoff=0)
mnu1.add_command(label='New file')
mnu1.add_command(label='Open file')
mnu1.add_command(label='New')
mnu1.add_command(label='Save')
mnu1.add_command(label='Save as')
mnu1.add_command(label='Exit', command=myApp.quit)
mnuBar.add_cascade(label='File1', menu=mnu)
myApp.config(menu=mnuBar)


myApp.mainloop()

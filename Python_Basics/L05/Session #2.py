"""
========================================
-----> intro. to GUI with Tkinter <-----
========================================
"""
from tkinter import *
from tkinter import ttk

# ازاي تبدأ الواجهه
App = Tk()

# التحكم في ابعاد الواجهه
App.geometry('400x500+500+200')

# منع او السماح للمستخدم بالتحكم في ابعاد الواجهه
App.resizable(True, True)

# تغيير عنوان البرنامج
App.title('Aladdin')

# تغيير لون خلفية واجهة البرنامج
App.config(background='#8ab2f1')

# تغير ايقونة البرنامج
# (يجب ان تكون الصورة محفوظه علي جهازك و ان تكون ب امتداد .ico)
App.iconbitmap(r'D:\Python\files\twitter.ico')

# اقصى حد يمكن تصغير البرنامج اليه
App.minsize(300,400)

# اقصى حد يمكن تكبير البرنامج اليه
App.maxsize(600, 700)

# انشاء قسم في واجهة البرنامج
frm = Frame(App, width=600, height=80, bg='silver')
# اضافة ذلك القسم الى البرنامج
frm.pack()

# اضافة ازرار
btm1 = Button(frm, width=12, height=1, text='Login', cursor='tcross')
btm1.place(x=250, y=50)

# اضافة نص ثابت
lbl1 = Label(frm, text='Username :', bg='silver')
lbl1.place(x=10, y=10)

# صندوق ادخال
entr = Entry(frm)
entr.place(x=80, y=12)

# قائمة اختيار من متعدد
lbl2 = Label(frm, text="City", bg='silver')
lbl2.place(x=10, y=35)
cmbx = ttk.Combobox(frm, values=[
    'Cairo', "Mansoura", "Giza", "Alex", 'Port-Said'
], state='readonly')
cmbx.place(x=45, y=38)

# اهم سطر وهو المسؤول عن اظهار البرنامج وتفعيله
App.mainloop()
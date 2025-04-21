from tkinter import *

# ---- start ----
login_App = Tk()
login_App.geometry('600x600')
login_App.resizable(False, False)
login_App.config(background='#aab7b8')
login_App.title("Login System")
login_App.iconbitmap(r'D:\Python\files\securityBitMap.ico')
# ---- Title ----
title = Label(
    login_App, text='Log IN',
    font=('Courier', 15, 'bold'), bg="#566573", fg='white'
)
title.pack(fill=X)
# ---- Frame ----
frm1 = Frame(login_App, width=390, height=420, bg='whiteSmoke')
frm1.pack(pady=35)
# ---- Image ----
photo = PhotoImage(file=r'D:\Python\files\login.png')
rePhoto = photo.subsample(20, 20)
lbl = Label(login_App, image=rePhoto)
lbl.place(x=230, y=65)
# ---- Labels ----
lbl1 = Label(
    frm1, text='UserName :', font=('Courier', 15), bg='whiteSmoke'
)
lbl1.place(x=10, y=180)
lbl2 = Label(
    frm1, text='Password :', font=('Courier', 15), bg='whiteSmoke'
)
lbl2.place(x=10, y=220)
# ---- Entry ----
ent1 = Entry(frm1)
ent1.place(x=139, y=185)
ent2 = Entry(frm1)
ent2.place(x=139, y=225)
# ---- Buttons ----
btn1 = Button(
    frm1, text='Login', font=('Courier', 10), bg='#d5f5e3', width=15
)
btn1.place(x=60, y=300)
btn2 = Button(
    frm1, text='Cancel', font=('Courier', 10), bg='#f2d7d5', width=15
)
btn2.place(x=215, y=300)
# ---- Check Box ----
chk = Checkbutton(
    frm1, text='Agreed with terms',
    font=('Courier', 12), bg='whiteSmoke')
chk.place(x=22, y=260)
# ---- Developed by ----
Name = Label(
    frm1, text='Developed by Aladdin @2024',
    font=('Courier', 9), bg='whiteSmoke')
Name.place(x=100, y=396)
# ---- End ----
login_App.mainloop()

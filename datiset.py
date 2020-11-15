from tkinter import *
import os

window = Tk()

# add widgets here
print('\033[91m datiset program created by\033[0m' + '\033[35m--*ANTU VARGHESE*-- \033[0m')
print("plz enter date in \033[91m mm/dd/yyyy\033[0m format (eg:-06/25/2020)")
print("plz enter time in \033[91m hh:mm:ss\033[0m format(eg:-10:00:00AM)")

lbl = Label(window, text="Date:", fg="red")
lbl.place(x=10, y=20)


def date_change(dvalue):
    os.system('date -s %s' % dvalue)


e1 = Entry(window)
e1.place(x=40, y=50)

btn = Button(window, text="SET", border=3, command=lambda: date_change(e1.get()))
btn.place(x=70, y=80)

lbl2 = Label(window, text="Time:", fg="red")
lbl2.place(x=10, y=110)


def time_change(tvalue):
    os.system('date -s %s' % tvalue)


e2 = Entry(window)
e2.place(x=40, y=140)

btn = Button(window, text="SET", border=3, command=lambda: date_change(e2.get()))
btn.place(x=70, y=170)

btn = Button(window, text="EXIT", border=5, width=10, command=window.destroy)
btn.place(x=80, y=220)

lbl3 = Label(window, text="Credits:", fg="darkgreen")
lbl3.place(x=40, y=260)
lbl4 = Label(window, text="-+*ANTU VARGHESE*+-               v1.5", fg="darkred")
lbl4.place(x=90, y=260)
window.title("DATISET")
window.geometry("300x300")
window.mainloop()

'''
Write a python program using Tkinter interface to create a frame of size (400,400) that
has
1. Label - FirstName and Entry to take the name
2. Label - LastName and Entry to take the last name
3. Label - Email ID and Entry to take the E-mail
4. Label - Contact number and Entry to take the phone number
5. Button - Submit , when clicked on this button, a messagebox needs to pop out with printing all these details into
the messagebox
'''























from tkinter import *
import tkinter.messagebox
window = Tk()
window.title("Registration Form")
window.geometry('400x400')
window.configure(background = "grey")
a = Label(window ,text = "First Name")
b = Label(window ,text = "Last Name")
c = Label(window ,text = "Email Id")
d = Label(window ,text = "Contact Number")
a1 = Entry(window)
b1 = Entry(window)
c1 = Entry(window)
d1 = Entry(window)
def clicked():
    res = "The details are\n " + str(a1.get()) + "\n" + str(b1.get())+ "\n" + str(c1.get()) + "\n" + str(d1.get())
    tkinter.messagebox.showinfo("RESULT"," "+res)

btn = Button(window ,text="Submit",command=clicked)
a.pack()
a1.pack()
b.pack()
b1.pack()
c.pack()
c1.pack()
d.pack()
d1.pack()
btn.pack()
window.mainloop()
from re import T
import tkinter
from tkinter import *
from tkinter.ttk import *

root = Tk()

root.iconbitmap("face.ico")
root.title('Testing GUI')
root.geometry('250x400')


"""Storing gender Checkbutton widget value in a string variable"""
checkgender = StringVar()
checkgender = StringVar()
checkgender = StringVar()


"""Name Input using Entry Widget"""
lab1 = Label(root, text="Enter your name").grid(row=0, column=0)
ent =  Entry(root)
ent.grid(row=0, column=1)

"Age input using Scale Widget"
lab2 = Label(root, text="Enter age below").grid(row=1, column=0)
age_scale = Scale(root, from_=7, to=80, orient=HORIZONTAL)
age_scale.grid(row=1, column=1)

"""Gender input using Checkbutton Widget"""
lab3 = Label(root, text="Select your gender").grid(row=2, column=0)
gender_check = Checkbutton(root, text="Male",variable=checkgender ,onvalue="Male", offvalue="None")
gender_check.grid(row=2, column=1)
gender_check = Checkbutton(root, text="Female",variable=checkgender, onvalue="Female", offvalue="None")
gender_check.grid(row=3, column=1)
gender_check = Checkbutton(root, text="Both",variable=checkgender, onvalue="Both", offvalue="None")
gender_check.grid(row=4, column=1)

"""Email input"""
lab4 = Label(root, text="Enter your email below")
lab4.grid(columnspan=2)
en3 = Entry(root)
en3.grid(columnspan=2, pady=5)

"""Number input"""
lab5 = Label(root, text="Enter your mobile number below")
lab5.grid(columnspan=2)
ent4 = Entry(root)
ent4.grid(columnspan=2, pady=5)



"""Function to display the info for our Buttons"""
def clicked():

    """Creating another window using Toplevel widget"""
    Top = Toplevel()
    Top.title("Your details")
    Top.geometry('250x400')

    """Getting user's name"""

    lab4 = Label(Top, text="Your name is : ")
    lab4.grid(row=0, column=0, pady=10)
    name = ent.get()
    showname = Label(Top, text=name)
    showname.grid(row=0, column=1)

    """Getting user's age"""

    lab5 = Label(Top, text="Your age is : ")
    lab5.grid(row=1, column=0, pady=10)
    age = age_scale.get()
    showage = Label(Top, text=age)
    showage.grid(row=1, column=1)

    """Getting user's gender"""

    lab6 = Label(Top, text="Your Gender is : ")
    lab6.grid(row=2, column=0, pady=10)
    gender = checkgender.get()
    showgender = Label(Top, text=gender)
    showgender.grid(row=2, column=1)


    """Getting user email"""
    lab7 = Label(Top, text="Your Email id is : ")
    lab7.grid(row=3, column=0, pady=10)
    email = en3.get()
    show_email = Label(Top, text=email)
    show_email.grid(row=3, column=1)

    
    """Getting user number"""
    lab8 = Label(Top, text="Your mobile number is : ")
    lab8.grid(row=4, column=0)
    number = ent4.get()
    show_number = Label(Top, text=number)
    show_number.grid(row=4, column=1)


"""Submit button"""
btn = Button(root, text="Submit", command=clicked).grid(columnspan=2, pady=5)


"""Exit button"""
exit_btn = Button(root, text="Exit", command= root.destroy)
exit_btn.grid(columnspan=2)


root.mainloop()
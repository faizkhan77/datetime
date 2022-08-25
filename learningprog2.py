
import tkinter
from tkinter import *
import datetime

root = Tk()
root.geometry("450x300")

def weekday():
    weekday_check = datetime.datetime.now()
    abc = weekday_check.strftime("%A")
    lab = Label(root, text=abc).pack()
    
def month():
    month_check = datetime.datetime.now()
    abc = month_check.strftime("%B")
    lab = Label(root, text=abc).pack()

def year():
    year_check = datetime.datetime.now()
    abc = year_check.strftime("%Y")
    lab = Label(root, text=abc).pack()


btn1 = Button(root, text="Check Weekday", command=weekday)
btn1.pack(pady=10)

btn2 = Button(root, text="Check Month", command=month)
btn2.pack(pady=10)

btn3 = Button(root, text="Check year", command=year)
btn3.pack(pady=10)



root.mainloop()


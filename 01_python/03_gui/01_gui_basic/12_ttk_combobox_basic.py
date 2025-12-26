import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

values = [str(i) + " day" for i in range(1, 32)]  # numbers from 1 to 31
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("Payment Due Date")  # set default text

def btncmd():
    print(combobox.get())  # display selected value

btn = Button(root, text="Select", command=btncmd)
btn.pack()

root.mainloop()

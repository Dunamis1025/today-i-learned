import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

values = ["    Day " + str(i) for i in range(1, 32)]  # numbers from 1 to 31
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("Payment Due Date")  # set default text

readonly_combobox = ttk.Combobox(
    root,
    height=10,
    values=values,
    state="readonly"  # read-only combobox
)
readonly_combobox.current(0)  # select the item at index 0
readonly_combobox.pack()

def btncmd():
    print(combobox.get())          # display selected value
    print(readonly_combobox.get()) # display selected value from readonly combobox

btn = Button(root, text="Select", command=btncmd)
btn.pack()

root.mainloop()

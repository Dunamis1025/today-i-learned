import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

# Progress bar moves back and forth (indeterminate mode)
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")

# Progress bar fills from left to right (determinate mode)
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10)  # moves every 10 ms (using 1 makes it move much faster)
progressbar.pack()

def btncmd():
    progressbar.stop()  # stop the progress bar

btn = Button(root, text="Stop", command=btncmd)
btn.pack()

root.mainloop()

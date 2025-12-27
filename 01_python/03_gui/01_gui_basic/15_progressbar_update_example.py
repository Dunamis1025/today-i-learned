import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

# Progress bar moves back and forth (indeterminate mode)
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")

# Progress bar fills from left to right (determinate mode)
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)  # moves every 10 ms (using 1 makes it move much faster)
# progressbar.pack()

# def btncmd():
#     progressbar.stop()  # stop the progress bar

# btn = Button(root, text="Stop", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(
    root,
    maximum=100,
    length=150,
    variable=p_var2
)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):  # range from 1 to 100
        time.sleep(0.01)     # wait for 0.01 seconds

        p_var2.set(i)        # set the progress bar value
        progressbar2.update()  # force UI update
        print(p_var2.get())  # print current value to the console

btn = Button(root, text="Start", command=btncmd2)
btn.pack()

root.mainloop()

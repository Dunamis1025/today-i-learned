from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "Please enter text")

e = Entry(root, width=30)
e.pack()
e.insert(0, "Enter a single line")

def btncmd():
    # Print contents
    print(txt.get("1.0", END))  # line 1, column 0
    print(e.get())

    # Clear contents
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()

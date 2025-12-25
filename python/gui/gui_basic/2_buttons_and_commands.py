from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="Button 1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="Button 2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="Button 3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="Button 4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="Button 5")
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("Button clicked")

btn7 = Button(root, text="Working Button", command=btncmd)
btn7.pack()

root.mainloop()

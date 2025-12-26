from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

Label(root, text="Please select a menu").pack()

burger_var = IntVar()  # store the selected burger value as an integer

btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger1.select()  # set Hamburger as the default selection

btn_burger2 = Radiobutton(root, text="Cheeseburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Chicken Burger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="Please select a drink").pack()

drink_var = StringVar()  # store the selected drink value as a string

btn_drink1 = Radiobutton(root, text="Cola", value="Cola", variable=drink_var)
btn_drink1.select()  # set Cola as the default selection

btn_drink2 = Radiobutton(root, text="Sprite", value="Sprite", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get())  # prints the value of the selected burger
    print(drink_var.get())   # prints the value of the selected drink

btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()

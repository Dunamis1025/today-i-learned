from tkinter import *

# Create the main application window
root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

# Top function key row
btn_f16 = Button(root, text="F16")
btn_f17 = Button(root, text="F17")
btn_f18 = Button(root, text="F18")
btn_f19 = Button(root, text="F19")

btn_f16.grid(row=0, column=0)
btn_f17.grid(row=0, column=1)
btn_f18.grid(row=0, column=2)
btn_f19.grid(row=0, column=3)

# Clear / operator row
btn_clear = Button(root, text="Clear")
btn_equal = Button(root, text="=")
btn_div = Button(root, text="/")
btn_mul = Button(root, text="*")

btn_clear.grid(row=1, column=0)
btn_equal.grid(row=1, column=1)
btn_div.grid(row=1, column=2)
btn_mul.grid(row=1, column=3)

# Number row starting with 7
btn_7 = Button(root, text="7")
btn_8 = Button(root, text="8")
btn_9 = Button(root, text="9")
btn_sub = Button(root, text="-")

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_sub.grid(row=2, column=3)

# Number row starting with 4
btn_4 = Button(root, text="4")
btn_5 = Button(root, text="5")
btn_6 = Button(root, text="6")
btn_add = Button(root, text="+")

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_add.grid(row=3, column=3)

# Number row starting with 1
btn_1 = Button(root, text="1")
btn_2 = Button(root, text="2")
btn_3 = Button(root, text="3")
btn_enter = Button(root, text="Enter")  # Should span vertically

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_enter.grid(row=4, column=3, rowspan=2)  # Span downward across two rows

# Bottom row starting with 0
btn_0 = Button(root, text="0")  # Should span horizontally
btn_point = Button(root, text=".")

btn_0.grid(row=5, column=0, columnspan=2)  # Span across two columns
btn_point.grid(row=5, column=2)

# Start the Tkinter event loop
root.mainloop()

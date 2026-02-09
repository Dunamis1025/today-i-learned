from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width x height

# Listbox widget
# selectmode:
# - "single"   : allows selecting only one item at a time
# - "extended" : allows selecting multiple items (Ctrl / Shift)
#
# height:
# - 0 : automatically shows all items
# - N : shows only N items (e.g. height=3 shows up to 3 items)
#
# Scrollbars will be covered later
listbox = Listbox(root, selectmode="extended", height=0)

listbox.insert(0, "Apple")
listbox.insert(1, "Strawberry")
listbox.insert(2, "Banana")
listbox.insert(END, "Watermelon")
listbox.insert(END, "Grape")
listbox.pack()

def btncmd():
    # Delete items from the listbox
    # - END : removes the last item
    # - 0   : removes the first item
    # listbox.delete(END)

    # Print the current number of items in the listbox
    # print("Number of items in the listbox:", listbox.size())

    # Get items from index 0 to 2 (inclusive)
    # print("Items from index 0 to 2:", listbox.get(0, 2))

    # Check which items are currently selected
    # curselection() returns a tuple of selected indices
    print("Selected item indices:", listbox.curselection())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()

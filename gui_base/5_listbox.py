from tkinter import *

root = Tk()
root.title("Juno GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()


def btncmd():
    # Delete
    # listbox.delete(END)  # Delete the last list.
    # listbox.delete(0)  # Delete the first list.

    # Count the number of list
    # print("The number of list :", listbox.size())

    # Check the list
    # print("From the first and third list :", listbox.get(0, 2))

    # Check the selected list (Return the index. EX: (1, 2, 3))
    print("The selected list: ", listbox.curselection())


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
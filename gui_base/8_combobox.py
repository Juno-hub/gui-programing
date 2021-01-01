import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Juno GUI")
root.geometry("640x480")

values = [str(i) + " day" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("Card Payment date")  # Title or set a value through button click

readonly_combobox = ttk.Combobox(root,
                                 height=10,
                                 values=values,
                                 state="readonly")
readonly_combobox.current(0)  # index: 0
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())


btn = Button(root, text="Choice", command=btncmd)
btn.pack()

root.mainloop()
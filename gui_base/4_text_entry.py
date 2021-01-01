from tkinter import *

root = Tk()
root.title("Juno GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "Enther the literal")

e = Entry(root, width=30)
e.pack()
e.insert(0, "Enter the one line.")


def btncmd():
    # Return the contend
    print(txt.get("1.0", END))  # "1": row, "0": column
    print(e.get())
    # Delete the contend
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
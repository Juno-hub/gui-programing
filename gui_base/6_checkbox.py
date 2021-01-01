from tkinter import *

root = Tk()
root.title("Juno GUI")
root.geometry("640x480")

chkvar = IntVar()  # int type is saved in chkvar
chkbox = Checkbutton(root, text="To not see me today", variable=chkvar)
# chkbox.select()  # Already checked
# chkbox.deselect()  # Already not checked
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="To not see me 1 week", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get())  # 0 : not checked, 1 : checked
    print(chkvar2.get())


btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()
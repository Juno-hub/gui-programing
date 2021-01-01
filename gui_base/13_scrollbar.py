from tkinter import *

root = Tk()
root.title("Juno GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# If you don't set "set", when scroll get down, but scroll get up.
listbox = Listbox(frame,
                  selectmode="extended",
                  height=10,
                  yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + " Day")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()
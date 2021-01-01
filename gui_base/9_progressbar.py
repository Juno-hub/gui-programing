import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Juno GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)  # Move by 10 ms
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text="Stop!", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=200, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(101):
        time.sleep(0.01)  # wait 0.01 second

        p_var2.set(i)  # set value of progress bar
        progressbar2.update()  # UI update
        print(p_var2.get())


btn = Button(root, text="Start!", command=btncmd2)
btn.pack()

root.mainloop()
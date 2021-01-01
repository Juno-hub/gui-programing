from tkinter import *

root = Tk()
root.title("Juno GUI")
root.geometry("640x480")

label1 = Label(root, text="Hello World!")
label1.pack()

photo = PhotoImage(file="img.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="See you again")

    global photo2  # If variable sets the global variable, it avoid to delete from grabage collection
    photo2 = PhotoImage(file="img2.png")
    label2.config(image=photo2)


btn = Button(root, text="Click", command=change)
btn.pack()

root.mainloop()
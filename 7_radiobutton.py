from tkinter import *

root = Tk()
root.title("Juno GUI")
root.geometry("640x480")

Label(root, text="Select the menu").pack()

burger_var = StringVar()
btn_burger1 = Radiobutton(root,
                          text="Hamburger",
                          value="Hamburger",
                          variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root,
                          text="Cheese burger",
                          value="Cheese burger",
                          variable=burger_var)
btn_burger3 = Radiobutton(root,
                          text="Chicken burger",
                          value="Chicken burger",
                          variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="Select the drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="Coke", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="Soda", value="Soda", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())
    print(drink_var.get())


btn = Button(root, text="Order", command=btncmd)
btn.pack()

root.mainloop()
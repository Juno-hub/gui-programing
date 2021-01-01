from tkinter import *

root = Tk()
root.title("Juno GUI")
root.geometry("640x480")

Label(root, text="Select the menu").pack(side="top")

Button(root, text="Order").pack(side="bottom")
# Menu Frame
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheese burger").pack()
Button(frame_burger, text="Chicken burger").pack()

# Drink Frame
frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Soda").pack()

root.mainloop()
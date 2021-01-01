import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Juno GUI")
root.geometry("640x480")


# Train ticketing system
def info():
    msgbox.showinfo("Info", "Complete the ticketing.")


def warn():
    msgbox.showwarning("Warning", "The seat is sold out.")


def error():
    msgbox.showerror("Error", "Payment Error")


def okcancel():
    msgbox.askokcancel("OK / Cancel",
                       "The seat is for child to accompany. Do you want?")


def retrycancel():
    response = msgbox.askretrycancel(
        "Retry / Cancel", "It's error is temporary. How about try again?")
    if response == 1:  # Retry
        print("Retry")
    elif response == 0:  # Cancel
        print("Cancel")


def yesno():
    msgbox.askyesno("Yes / No",
                    "It is a backward-facing seat. Do you ticketing it?")


def yesnocancel():
    response = msgbox.askyesnocancel(
        title=None,
        message=
        "This content is not saved.\nAre you sure want to save and exit?")
    # 예(Y) : Save and Exit
    # 아니오(N) : No save and Exit
    # 취소(Cancel) : Cancel
    print("Response :", response)  # True, False, None -> Yse = 1, No = 0, else
    if response == 1:  # Yes
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")


Button(root, command=info, text="Info").pack()
Button(root, command=warn, text="Warning").pack()
Button(root, command=error, text="Error").pack()

Button(root, command=okcancel, text="Ok and Cancel").pack()
Button(root, command=retrycancel, text="Retry and Cancel").pack()
Button(root, command=yesno, text="Yes or No").pack()
Button(root, command=yesnocancel, text="Yes No Cancel").pack()
root.mainloop()
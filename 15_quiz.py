# Q) Make the notepad program using tkinter

# [Rule]
# 1. title : 제목없음 - Windows 메모장
# 2. Such as Windows notepad, same menu
# 3. It is implemented that "열기, 저장, 끝내기"
# 3-1: 열기 : Open mynote.txt, show the content on the file.
# 3-2: 저장 : Save the content on mynote.txt
# 3-3: 끝내기 : Exit
# 4. When program start, the content is clear.
# 5. Regardless of bottom status bar
# 6. Frame size, loacation is free but, you can control the size.
# 7. Insert scroll bar rightwards the content.

from tkinter import *

root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("680x450")


def open_file():
    with open("mynote.txt", "r", encoding="utf8") as open_notepad:
        txt.delete("1.0", END)
        txt.insert(END, open_notepad.read())


def save_file():
    with open("mynote.txt", "w", encoding="utf8") as save_notepad:
        save_notepad.write(txt.get("1.0", END))


menu = Menu(root)
# File Menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# Edit Menu
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집")

# Templeate Menu
menu.add_cascade(label="서식")

# View Menu
menu.add_cascade(label="보기")

# Help Menu
menu.add_cascade(label="도움말")

#scroll-bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Text
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", expand=True, fill="both")

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()
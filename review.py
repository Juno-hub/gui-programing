import os
import time
from tkinter import *
from PIL import Image
import tkinter.ttk as ttk
from tkinter import filedialog
import tkinter.messagebox as msgbox

title = "Juno GUI"
root = Tk()
root.title(title)


def combine_image():
    try:
        # 가로넓이
        image_width = combo_width.get()
        if image_width == "원본유지":
            image_width = -1
        else:
            image_width = int(image_width)
        # 간격
        image_space = combo_space.get()
        if image_space == "없음":
            image_space = 0
        elif image_space == "좁게":
            image_space = 30
        elif image_space == "보통":
            image_space = 60
        else:
            image_space = 90
        # 저장형식
        image_format = combo_format.get().lower()

        images = [Image.open(x) for x in listbox.get(0, END)]

        # 이미지 사이즈 리스트
        image_sizes = []
        if image_width > -1:
            image_sizes = [(int(image_width),
                            int(image_width) * x.size[1] / x.size[0])
                           for x in images]
        else:  # 원본유지
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*(image_sizes))

        max_width, total_height = max(widths), sum(heights)

        # 스케치북 만들기
        if image_space > 0:
            total_height += (image_space * (len(images) - 1))

        result_image = Image.new("RGB", (max_width, total_height),
                                 (255, 255, 255))

        y_offset = 0

        for index, image in enumerate(images):
            if image_width > 1:
                image = image.resize(image_sizes[index])

            result_image.paste(image, (0, y_offset))
            y_offset += (image.size[1] + image_space)

            progress = (index + 1) / len(images) * 100
            p_var.set(progress)
            progress_bar.update()

        # 저장형식
        current_time = time.strftime("%Y-%m-%d_%H%M%S")
        file_name = current_time + "." + image_format
        _path = os.path.join(file_path.get(), file_name)
        result_image.save(_path)
        msgbox.showinfo(title, "이미지 합치기가 완료되었습니다")
    except Exception as err:
        msgbox.showerror(title, err)


# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(
        title=title,
        filetypes=(("이미지 파일", "*.png;*.jpg;*.bmp"), ("모든파일", "*.*")),
        initialdir=r"C:\Users\82108\Documents\gui-programing\images")
    for file in files:
        listbox.insert(END, file)


def del_file():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)


def find_folder():
    selected_folder = filedialog.askdirectory()
    if selected_folder == '':
        return
    file_path.delete(0, END)
    file_path.insert(0, selected_folder)


def start():
    if listbox.size() == 0:
        msgbox.showerror(title, "이미지 파일을 추가해주세요")
        return
    if len(file_path.get()) == 0:
        msgbox.showerror(title, "파일을 저장할 폴더를 선택해주세요")
        return
    combine_image()


# 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

# 파일 추가, 선택 삭제 버튼
btn_add_file = Button(file_frame,
                      text="파일 추가",
                      padx=5,
                      pady=5,
                      width=10,
                      command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame,
                      text="선택 삭제",
                      padx=5,
                      pady=5,
                      width=10,
                      command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="x", padx=5, pady=5)

# 스크롤바, 리스트 박스
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(list_frame,
                  selectmode="extended",
                  height=15,
                  yscrollcommand=scrollbar.set)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listbox.yview)

# 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5)

# 엔트리, 찾아보기 버튼
file_path = Entry(path_frame)
file_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_find_folder = Button(path_frame,
                         text="찾아보기",
                         width=10,
                         command=find_folder)
btn_find_folder.pack(side="right", padx=5, pady=5)

# 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(padx=5, pady=5)

# 가로넓이
label_width = Label(option_frame, text="가로넓이", width=8)
label_width.pack(side="left", padx=5, pady=5)

width_option = ["원본유지", "1024", "800", "640"]
combo_width = ttk.Combobox(option_frame,
                           state="readonly",
                           values=width_option,
                           width=10)
combo_width.current(0)
combo_width.pack(side="left", padx=5, pady=5)
# 간격
label_space = Label(option_frame, text="간격", width=8)
label_space.pack(side="left", padx=5, pady=5)

space_option = ["없음", "좁게", "보통", "넓게"]
combo_space = ttk.Combobox(option_frame,
                           state="readonly",
                           values=space_option,
                           width=10)
combo_space.current(0)
combo_space.pack(side="left", padx=5, pady=5)
# 저장형식
label_format = Label(option_frame, text="저장형식", width=8)
label_format.pack(side="left", padx=5, pady=5)

format_option = ["PNG", "JPG", "BMP"]
combo_format = ttk.Combobox(option_frame,
                            state="readonly",
                            values=format_option,
                            width=10)
combo_format.current(0)
combo_format.pack(side="left", padx=5, pady=5)

# 진행상황 프레임
progress_frame = LabelFrame(root, text="진행상황")
progress_frame.pack(fill="x", padx=5, pady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# 시작 & 닫기 프레임
start_exit_frame = Frame(root)
start_exit_frame.pack(side="right", padx=5, pady=5)

btn_exit = Button(start_exit_frame,
                  text="닫기",
                  command=root.quit,
                  padx=5,
                  pady=5,
                  width=10)
btn_exit.pack(
    side="right",
    padx=5,
    pady=5,
)

btn_start = Button(start_exit_frame,
                   text="시작하기",
                   padx=5,
                   pady=5,
                   width=10,
                   command=start)
btn_start.pack(
    side="right",
    padx=5,
    pady=5,
)

root.resizable(False, False)
root.mainloop()
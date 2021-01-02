import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Juno GUI")


# Combine images
def combine_image():
    try:
        # Width
        img_width = cmb_width.get()
        if img_width == "Original":
            img_width = -1
        else:
            img_width = int(img_width)

        # Interval
        img_interval = cmb_interval.get()
        if img_interval == "small":
            img_interval = 30
        elif img_interval == "normal":
            img_interval = 60
        elif img_interval == "large":
            img_interval = 90
        else:
            img_interval = 0

        # Format
        img_format = cmb_format.get().lower()

        images = [Image.open(x) for x in list_file.get(0, END)]

        # Image size list
        image_sizes = []  # [(width1, height1), (width2, height2), ...]
        if img_width > -1:  # change the width value
            image_sizes = [(int(img_width),
                            int(img_width * x.size[1] / x.size[0]))
                           for x in images]
        else:
            # original size
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        widths, heights = zip(*(image_sizes))

        # Get the max width, the total height
        max_width, total_height = max(widths), sum(heights)

        # Scketchbook
        # Backgroud white
        if img_interval > 0:
            total_height += (img_interval * (len(images) - 1))

        result_img = Image.new("RGB", (max_width, total_height),
                               (255, 255, 255))
        y_offset = 0  # y location

        for idx, img in enumerate(images):
            if img_width > 1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_interval)

            progress = (idx + 1) / len(images) * 100
            p_var.set(progress)
            progress_bar.update()

        # Format option
        file_name = "juno_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("Information", "Complementation")
    except Exception as err:
        msgbox.showerror("Error", err)


# Add a file & Delete a file
def add_file():
    files = filedialog.askopenfilenames(
        title="Select the image file",
        filetypes=(("PNG file", "*.png"), ("All of file", "*.*")),
        initialdir=r"C:\Users\82108\Documents\gui-programing"
    )  # Show the initial path user specifies.
    for file in files:
        list_file.insert(END, file)


def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


def browse_dest_path():
    selected_folder = filedialog.askdirectory()
    if selected_folder == '':  # if selected_folder == ": ??
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, selected_folder)


def start():
    # Option value
    # print("Width: ", cmb_width.get())
    # print("Interval: ", cmb_interval.get())
    # print("File format: ", cmb_format.get())

    # File list
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Add an image file")
        return

    # Saved path
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Select the saved file")
        return

    combine_image()


# File frame (Add a file, Delete)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame,
                      padx=5,
                      pady=5,
                      width=12,
                      text="Add a file",
                      command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame,
                      padx=5,
                      pady=5,
                      width=12,
                      text="Delete",
                      command=del_file)
btn_del_file.pack(side="right")

# List frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame,
                    selectmode="extended",
                    height=15,
                    yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Path frame
path_frame = LabelFrame(root, text="Saved path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5,
                   ipady=4)  # Inner hieght padding

btn_dest_frame = Button(path_frame,
                        text="Find",
                        width=10,
                        command=browse_dest_path)
btn_dest_frame.pack(side="right", padx=5, pady=5)

# Option frame
option_frame = LabelFrame(root, text="Option")
option_frame.pack(padx=5, pady=5, ipady=5)

# Width option
lbl_width = Label(option_frame, text="Width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(option_frame,
                         state="readonly",
                         values=opt_width,
                         width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)
# Interval option
lbl_interval = Label(option_frame, text="Interval", width=8)
lbl_interval.pack(side="left", padx=5, pady=5)

opt_interval = ["None", "small", "normal", "large"]
cmb_interval = ttk.Combobox(option_frame,
                            state="readonly",
                            values=opt_interval,
                            width=10)
cmb_interval.current(0)
cmb_interval.pack(side="left", padx=5, pady=5)
# Format option
lbl_format = Label(option_frame, text="File format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame,
                          state="readonly",
                          values=opt_format,
                          width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# Progress bar
progress_frame = LabelFrame(root, text="Progress")
progress_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Start & Exit frame
start_exit_frame = Frame(root)
start_exit_frame.pack(fill="x", padx=5, pady=5)

btn_exit = Button(start_exit_frame,
                  padx=5,
                  pady=5,
                  width=12,
                  text="Exit",
                  command=root.quit)
btn_exit.pack(side="right", padx=5, pady=5)

btn_start = Button(start_exit_frame,
                   padx=5,
                   pady=5,
                   width=12,
                   text="Start",
                   command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
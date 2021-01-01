import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Juno GUI")

# File frame (Add a file, Delete)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add a file")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete")
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
path_frame = LabelFrame(root, text="Save path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5,
                   ipady=4)  # Inner hieght padding

btn_dest_frame = Button(path_frame, text="Find", width=10)
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

btn_start = Button(start_exit_frame, padx=5, pady=5, width=12, text="Start")
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
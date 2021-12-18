from os import path
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename
from tkinter.font import Font

# sudo apt-get install python3-tk


def my_click():
    label["bg"] = "black"


def create_menu(master):
    my_menu = tk.Menu(master)
    master.config(menu=my_menu)
    file_menu = tk.Menu(my_menu, tearoff=False)
    file_menu.add_command(label="Open file", command=open_file)
    file_menu.add_command(label="Open file name", command=open_file_name)
    file_menu.add_command(label="New file")
    file_menu.add_separator()
    file_menu.add_command(label="Quit", command=master.quit)
    my_menu.add_cascade(label="File", menu=file_menu)


def open_file():
    res = askopenfile(title="open file to edit")
    print(res)


def open_file_name():
    path = askopenfilename(title="open file to edit")
    with open(path) as file:
        text_widget.insert("1.0", file.read())  # 1.0 = row.column
    print(path)


pyth = ["for", "in", "import", "if", "def"]

root_window = tk.Tk()
root_window.geometry("600x800")

create_menu(root_window)

s_var = tk.StringVar()
s_var.set("Hello dolly")
frame_left = tk.Frame(root_window, bg="#000")
frame_right = tk.Frame(root_window, bg="#555")
label = tk.Label(
    frame_left, textvariable=s_var,
    text="Hello I'm label", bg='blue', fg='#f40')
label.bind("<Button-1>", lambda evnt: showinfo("event", f"event info {evnt}"))
cbn = tk.Checkbutton(frame_left, text="I Agree")
text_widget = ScrolledText(frame_right, bg="#000", fg="green")  # ScrolledTExt
text_widget.tag_config("py", foreground="red", font=Font(family='Arial', slant="roman", weight="bold"))

entry_field = tk.Entry(frame_left, textvariable=s_var)
btn_ok = tk.Button(frame_left, text='OK')
btn_ok["command"] = lambda: showinfo(
    "hello", f"your input is: {entry_field.get()}")
# btn_ok["command"] = my_click
# pack - sides: top, lft, right, bootom
# place - x, y
# grid - cells
# label.pack()  # top
# label.pack(side=tk.LEFT)  # left
# Порядок зависит от порядка вызова .pack
frame_left.pack(side=tk.LEFT, fill="y")
frame_right.pack(side=tk.LEFT, fill="both", expand=True)
label.pack(side=tk.TOP, fill='x', expand=True)  # left
entry_field.pack(side='top', fill='x')
btn_ok.pack(side='top', fill='x')
cbn.pack(side='top', fill='y')
text_widget.pack(fill="both", expand=True)

# mainloop() must bee after .pack
root_window.mainloop()

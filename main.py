import random
import tkinter
from tkinter import messagebox

BG = "#24232b"
width = 400
height = 450

root = tkinter.Tk()
pass_length = tkinter.IntVar()
is_uppercase = tkinter.BooleanVar()
is_numbers = tkinter.BooleanVar()
is_symbols = tkinter.BooleanVar()


def get_length():
    return pass_length.get()


def slider_changed(event):
    value.config(text=get_length())


def generate():
    base = "abcdefghijklmnopqrstuvwxyz"
    new_pass = ""
    if is_uppercase.get():
        base += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if is_symbols.get():
        base += "!#$%&()*+"
    if is_numbers.get():
        base += "0123456789"

    for i in range(get_length()):
        new_pass += base[random.randint(0, len(base) - 1)]
    pass_label.config(text=new_pass)
    root.clipboard_append(new_pass)
    messagebox.showinfo("Information", "Copied to clipboard")
    print(new_pass)


# Root configuration
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.iconbitmap("password.ico")
root.config(bg=BG)
root.title("Password Generator | Jakub Olszak")
root.clipboard_clear()

# Heading Label
tkinter.Label(root,
              text="Password Generator",
              fg="#888597",
              bg=BG,
              font=('Lucida Sans', 20, 'normal')).pack(pady=20)

# Scale and Character Length section
tkinter.Scale(root,
              from_=0,
              to=32,
              orient='horizontal',
              bd=0,
              troughcolor="#18171f",
              bg=BG,
              command=slider_changed,
              variable=pass_length,
              highlightthickness=5,
              highlightbackground="#18171f",
              sliderlength=5,
              sliderrelief=tkinter.FLAT,
              showvalue=False).pack(pady=(0, 20), fill=tkinter.X, padx=20)

tkinter.Label(root,
              text="Character Length",
              fg="#e7e6ee",
              bg=BG,
              font=('Lucida Sans', 16, 'normal')).pack()

value = tkinter.Label(root,
                      text=get_length(),
                      fg="#acf3b5",
                      bg=BG,
                      font=('Lucida Sans', 16, 'normal'))
value.pack(pady=10)


# Checkbox Section
tkinter.Checkbutton(root,
                    activebackground=BG,
                    variable=is_uppercase,
                    highlightthickness=0,
                    selectcolor=BG,
                    text="Include Uppercase Letters",
                    font=('Luicida Sans', 16, 'normal'),
                    bg=BG,
                    fg="#ffffff",
                    anchor="w").pack(fill=tkinter.X, padx=20)

tkinter.Checkbutton(root,
                    activebackground=BG,
                    variable=is_numbers,
                    highlightthickness=0,
                    selectcolor=BG,
                    text="Include Numbers",
                    font=('Luicida Sans', 16, 'normal'),
                    bg=BG,
                    fg="#e7e6ee",
                    anchor="w").pack(fill=tkinter.X, padx=20)

tkinter.Checkbutton(root,
                    activebackground=BG,
                    variable=is_symbols,
                    highlightthickness=0,
                    selectcolor=BG,
                    text="Include Symbols",
                    font=('Luicida Sans', 16, 'normal'),
                    bg=BG,
                    fg="#e7e6ee",
                    anchor="w").pack(fill=tkinter.X, padx=20)

# Password Label
pass_label = tkinter.Label(root,
                           fg="#888597",
                           bg="#18171f",
                           font=('Lucida Sans', 16, 'normal'))
pass_label.pack(fill=tkinter.X, padx=20, pady=20)

# Button
tkinter.Button(root,
               activebackground="#acf3b5",
               text="GENERATE",
               fg=BG,
               bg="#acf3b5",
               font=('Luicida Sans', 12, 'bold'),
               command=generate).pack(fill=tkinter.X, padx=20, ipady=10)

root.mainloop()

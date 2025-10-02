import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")
root.configure(background="red")

# following minimum and maximum windowsize
# parameters don't seem to work
root.minsize(width=200, height=200)
root.maxsize(width=500, height=500)

# set initial windowsize
root.geometry("300x300+50+50")

# Create input field
entry1 = ttk.Entry(root, justify="right")
entry1.pack()

# Create Labels
label1 = tk.Label(root, text="aaaaa").pack()
label2 = tk.Label(root, text="bbbbb").pack()
# put widget to the left side and
# with the label at its bottom
label3 = tk.Label(root, text="Hello", anchor="s", width=20, height=5).pack(side="left")



root.mainloop()

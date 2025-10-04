# import tkinter, a GUI library
import tkinter as tk
from tkinter import ttk


def entry_insert_1():
    entry0.insert(tk.END, 1)
def entry_insert_2():
    entry0.insert(tk.END, 2)
def entry_insert_3():
    entry0.insert(tk.END, 3)
def entry_insert_4():
    entry0.insert(tk.END, 4)
def entry_insert_5():
    entry0.insert(tk.END, 5)
def entry_insert_6():
    entry0.insert(tk.END, 6)
def entry_insert_7():
    entry0.insert(tk.END, 7)
def entry_insert_8():
    entry0.insert(tk.END, 8)
def entry_insert_9():
    entry0.insert(tk.END, 9)
def entry_insert_plus():
    entry0.insert(tk.END, "+")
def print_entry():
    result = eval(str(entry0.get()))
    entry0.delete(0, tk.END)
    entry0.insert(0, result)
root = tk.Tk()
root.title("Calculator")
root.configure(background="lightblue")

# following minimum and maximum windowsize
# parameters don't seem to work
# root.minsize(width=200, height=200)
# root.maxsize(width=500, height=500)

# set initial windowsize
root.geometry("400x400")

# Create input field
entry0 = ttk.Entry(root, justify="right")
entry0.grid(row=0, column=0, columnspan=3, sticky="ew")

# Create button
# s
button1 = ttk.Button(root, text="1", command=entry_insert_1).grid(row=1, column=0, sticky="nsew")
button2 = ttk.Button(root, text="2", command=entry_insert_2).grid(row=1, column=1, sticky="nsew")
button3 = ttk.Button(root, text="3", command=entry_insert_3).grid(row=1, column=2, sticky="nsew")
button4 = ttk.Button(root, text="4", command=entry_insert_4).grid(row=2, column=0, sticky="nsew")
button5 = ttk.Button(root, text="5", command=entry_insert_5).grid(row=2, column=1, sticky="nsew")
button6 = ttk.Button(root, text="6", command=entry_insert_6).grid(row=2, column=2, sticky="nsew")
button7 = ttk.Button(root, text="7", command=entry_insert_7).grid(row=3, column=0, sticky="nsew")
button8 = ttk.Button(root, text="8", command=entry_insert_8).grid(row=3, column=1, sticky="nsew")
button9 = ttk.Button(root, text="9", command=entry_insert_9).grid(row=3, column=2, sticky="nsew")
button10 = ttk.Button(root, text="+", command=entry_insert_plus).grid(row=4, column=0, sticky="nsew")
button11 = ttk.Button(root, text="-").grid(row=4, column=1, sticky="nsew")
button12 = ttk.Button(root, text="=", command=print_entry).grid(row=4, column=2, sticky="nsew")
# put widget to the left side and
# with the button
#  at its bottom
# button
# 3 = ttk.Button(root, text="Hello", width=20).grid(row=0, column=3)

# Make the 3 columns fill
# the whole row equally
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

root.mainloop()


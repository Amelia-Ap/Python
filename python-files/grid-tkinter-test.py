import tkinter as tk
from tkinter import ttk


def say_hello():
	print("hello\n")

root = tk.Tk()
root.title("Calculator")
root.configure(background="lightblue")

# following minimum and maximum windowsize
# parameters don't seem to work
# root.minsize(width=200, height=200)
# root.maxsize(width=500, height=500)

# set initial windowsize
root.geometry("300x300+50+50")

# Create input field
entry0 = ttk.Entry(root, justify="right")
entry0.grid(row=0, column=0, columnspan=3, sticky="ew")

# Create Labels
label1 = ttk.Button(root, text="1").grid(row=1, column=0, sticky="nsew")
label2 = ttk.Button(root, text="2").grid(row=1, column=1, sticky="nsew")
label3 = ttk.Button(root, text="3").grid(row=1, column=2, sticky="nsew")
label4 = ttk.Button(root, text="4").grid(row=2, column=0, sticky="nsew")
label5 = ttk.Button(root, text="5").grid(row=2, column=1, sticky="nsew")
label6 = ttk.Button(root, text="6").grid(row=2, column=2, sticky="nsew")
label7 = ttk.Button(root, text="7").grid(row=3, column=0, sticky="nsew")
label8 = ttk.Button(root, text="8").grid(row=3, column=1, sticky="nsew")
label9 = ttk.Button(root, text="9").grid(row=3, column=2, sticky="nsew")
label10 = ttk.Button(root, text="+").grid(row=4, column=0, sticky="nsew")
label11 = ttk.Button(root, text="-").grid(row=4, column=1, sticky="nsew")
label12 = ttk.Button(root, text="=").grid(row=4, column=2, sticky="nsew")
# put widget to the left side and
# with the label at its bottom
# label3 = ttk.Button(root, text="Hello", width=20).grid(row=0, column=3)

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

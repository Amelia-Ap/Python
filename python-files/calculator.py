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
def entry_insert_minus():
    entry0.insert(tk.END, "-")
def entry_insert_times():
    entry0.insert(tk.END, "*")
def entry_insert_divide():
    entry0.insert(tk.END, "/")
def entry_insert_modulo():
    entry0.insert(tk.END, "%")
def entry_insert_point():
    entry0.insert(tk.END, ".")
def entry_insert_power():
    entry0.insert(tk.END, "**")
def entry_insert_point():
    entry0.insert(tk.END, ".")

def print_entry():
    result = entry0.get()
    '''
    print(f'num of 0s: {entry0.get().count(".")}')
    if (result.count(".") > 1):
        print("IP!!\n\n")
        for num in result.split("."):
            bin_byte = bin
            for k in (bin(int(num)))[2:]:
                print(k)
    result = eval(str(entry0.get()))
    entry0.delete(0, tk.END)
    entry0.insert(0, result)
    '''


for i in [123, 12, 255, 2]:
    print(f"number: {(bin(i)[2:])}",
          f"append to 0s: {(8-len(bin(i)[2:]))*"0"+(bin(i)[2:])}",
          f"number of dots: {len(bin(i)[2:])}")

#Create style
# style = ttk.Style()
# style.configure("Big.TButton", font=("Helvetica", 18))
# style.configure("Big.TEntry", font=("Helvetica", 48))
root = tk.Tk()
root.title("Calculator")
root.configure(background="lightblue")

# following minimum and maximum windowsize
# parameters don't seem to work
# root.minsize(width=200, height=200)
# root.maxsize(width=500, height=500)


# set initial windowsize
root.geometry("800x1000+50+50")

# Create input field
entry0 = ttk.Entry(root, justify="right")
entry0.grid(row=0, column=0, columnspan=3, pady=3, sticky="nsew")

# Create buttons
button1 = ttk.Button(root, text="1", command=entry_insert_1).grid(row=1, column=0, padx=3, pady=3, sticky="nsew")
button2 = ttk.Button(root, text="2", command=entry_insert_2).grid(row=1, column=1, padx=3, pady=3, sticky="nsew")
button3 = ttk.Button(root, text="3", command=entry_insert_3).grid(row=1, column=2, padx=3, pady=3, sticky="nsew")
button4 = ttk.Button(root, text="4", command=entry_insert_4).grid(row=2, column=0, padx=3, pady=3, sticky="nsew")
button5 = ttk.Button(root, text="5", command=entry_insert_5).grid(row=2, column=1, padx=3, pady=3, sticky="nsew")
button6 = ttk.Button(root, text="6", command=entry_insert_6).grid(row=2, column=2, padx=3, pady=3, sticky="nsew")
button7 = ttk.Button(root, text="7", command=entry_insert_7).grid(row=3, column=0, padx=3, pady=3, sticky="nsew")
button8 = ttk.Button(root, text="8", command=entry_insert_8).grid(row=3, column=1, padx=3, pady=3, sticky="nsew")
button9 = ttk.Button(root, text="9", command=entry_insert_9).grid(row=3, column=2, padx=3, pady=3, sticky="nsew")
button10 = ttk.Button(root, text="+", command=entry_insert_plus).grid(row=4, column=0, padx=3, pady=3, sticky="nsew")
button11 = ttk.Button(root, text="-", command=entry_insert_minus).grid(row=4, column=1, padx=3, pady=3, sticky="nsew")
button12 = ttk.Button(root, text=".", command=entry_insert_point).grid(row=4, column=2, padx=3, pady=3, sticky="nsew")
button13 = ttk.Button(root, text="*", command=entry_insert_times).grid(row=5, column=0, padx=3, pady=3, sticky="nsew")
button14 = ttk.Button(root, text="/", command=entry_insert_divide).grid(row=5, column=1, padx=3, pady=3, sticky="nsew")
button15 = ttk.Button(root, text="%", command=entry_insert_modulo).grid(row=5, column=2, padx=3, pady=3, sticky="nsew")
button15 = ttk.Button(root, text="^", command=entry_insert_power).grid(row=6, column=0, padx=3, pady=3, sticky="nsew")
button15 = ttk.Button(root, text="", command=entry_insert_point).grid(row=6, column=1, padx=3, pady=3, sticky="nsew")
button16 = ttk.Button(root, text="=", command=print_entry).grid(row=6, column=2, padx=3, pady=3, sticky="nsew")

# put widget to the left side and
# with the button at its bottom
# button3 = ttk.Button(root, text="Hello", width=20).grid(row=0, column=3)

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
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)

root.mainloop()

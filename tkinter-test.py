import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.configure(background="red")
root.minsize(200,200)
root.maxsize(500,500)
root.geometry("300x300+50+50")

# Create Labels
label1 = tk.Label(root, text="aaaaa").pack()
label2 = tk.Label(root, text="bbbbb").pack()
label3 = tk.Label(root, text="Hello", anchor="s", width=20, height=5).pack()
label2 = tk.W

root.mainloop()

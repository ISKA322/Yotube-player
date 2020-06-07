import tkinter as tk
import pywhatkit as kit

def get_entry():
    kit.playonyt((var.get()))


root = tk.Tk()
var = tk.StringVar()

ent = tk.Entry(root,textvariable = var)
btn2 = tk.Button(root, text="Play", command=get_entry)

ent.pack()
btn2.pack()

root.mainloop()
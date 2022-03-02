import tkinter as tk
from random import *

def write_slogan():
    print("")
def change():
    slogan["fg"] = "blue"
    slogan["text"] = "Bye"
    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="Hi", 
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   fg = "red",
                   command=change)
slogan.pack(side=tk.LEFT)

root.mainloop()

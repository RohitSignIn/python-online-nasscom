from tkinter import *
import tkinter.messagebox 

root = Tk()

# tkinter.messagebox.showinfo("Welcome to GFG", "East Button clicked")

# tkinter.messagebox.showwarning(title="Warning", message="I am Warning Box")

res = tkinter.messagebox.askyesno(title="Yes Or No", message="Do you want to continue")

print(res)

root.mainloop()
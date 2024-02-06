from tkinter import *
root = Tk()

def handleSubmit():
    print("Submit Button is Clicked")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

label1 = Label(root, text="Username", background="#2d2d2d", foreground="#fff", font=("helvetica", 28))
label1.grid(row=0, column=0, sticky="ewns")

entry1 = Entry(root, font=("helvetica", 38))
entry1.grid(row=0, column=1, sticky="ewns")

btn = Button(root, text="Submit", command=handleSubmit)
btn.grid(row=1, column=0, sticky="ewns")

root.mainloop()
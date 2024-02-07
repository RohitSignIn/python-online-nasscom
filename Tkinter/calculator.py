from tkinter import *
root = Tk()

root.title("Frame")
root.geometry("800x600")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)


frame1 = Frame(root)
frame1.grid(row=0, column=0, sticky="ewns")
frame1.columnconfigure(0, weight=1)


label1 = Label(frame1, text="123456789", font=("helvetica", 48))
label1.grid(row=0, column=0, sticky="ewns")

frame2 = Frame(root)
frame2.grid(row=1, column=0, sticky="ewns")
frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)
frame2.columnconfigure(2, weight=1)
frame2.columnconfigure(3, weight=1)


frame2.rowconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)
frame2.rowconfigure(2, weight=1)
frame2.rowconfigure(3, weight=1)


# Numbers
btn7 = Button(frame2, text="7")
btn8 = Button(frame2, text="8")
btn9 = Button(frame2, text="9") 
btn4 = Button(frame2, text="4")
btn5 = Button(frame2, text="5")
btn6 = Button(frame2, text="6")
btn1 = Button(frame2, text="1")
btn2 = Button(frame2, text="2")
btn3 = Button(frame2, text="3")
btn0 = Button(frame2, text="0")

# Operations
add = Button(frame2, text="+")
sub = Button(frame2, text="-")
mul = Button(frame2, text="*")
div = Button(frame2, text="/")
clr = Button(frame2, text="C")
run = Button(frame2, text="=")

btn7.grid(row=0, column=0, sticky="ewns")
btn8.grid(row=0, column=1, sticky="ewns")
btn9.grid(row=0, column=2, sticky="ewns")
btn4.grid(row=1, column=0, sticky="ewns")
btn5.grid(row=1, column=1, sticky="ewns")
btn6.grid(row=1, column=2, sticky="ewns")
btn1.grid(row=2, column=0, sticky="ewns")
btn2.grid(row=2, column=1, sticky="ewns")
btn3.grid(row=2, column=2, sticky="ewns")
btn0.grid(row=3, column=1, sticky="ewns")

add.grid(row=0, column=3, sticky="ewns")
sub.grid(row=1, column=3, sticky="ewns")
mul.grid(row=2, column=3, sticky="ewns")
div.grid(row=3, column=0, sticky="ewns")
clr.grid(row=3, column=2, sticky="ewns")
run.grid(row=3, column=3, sticky="ewns")


root.mainloop()
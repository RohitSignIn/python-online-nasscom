playerTurn = "x"

def handleBtnClick(btn):
    global playerTurn

    resRow = 0
    resColumn = btn-1

    if(btn >= 4 and btn <= 6):
        resRow=1
        resColumn = btn-4
    elif(btn > 6):
        resRow=2
        resColumn = btn-7

    btn = Button(layout, text=playerTurn, width=10, height=6)
    btn.grid(row=resRow, column=resColumn, padx=5, pady=5)

    if(playerTurn == "x"):
        playerTurn = "o"
    else: 
        playerTurn = "x"


from tkinter import *
root = Tk()

root.geometry("800x600")
root.title("Tic Tac Toe")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainFrame = Frame(root, background="#2d2d2d")
mainFrame.grid(row=0, column=0, sticky="ewns")

mainFrame.columnconfigure(0, weight=1)
mainFrame.rowconfigure(0, weight=1)

layout = Frame(mainFrame, background="#2d2d2d")
layout.grid(row=0, column=0)

btn1 = Button(layout, text="", width=10, height=6, command=lambda: handleBtnClick(1))
btn2 = Button(layout, text="", width=10, height=6, command=lambda: handleBtnClick(2))
btn3 = Button(layout, text="", width=10, height=6, command=lambda: handleBtnClick(3))
btn4 = Button(layout, text="", width=10, height=6, command=lambda: handleBtnClick(4))
btn5 = Button(layout, text="", width=10, height=6, command=lambda: handleBtnClick(5))
btn6 = Button(layout, text="", width=10, height=6, command=lambda: handleBtnClick(6))
btn7 = Button(layout, text="", width=10, height=6, command=lambda: handleBtnClick(7))
btn8 = Button(layout, text="", width=10, height=6, command=lambda: handleBtnClick(8))
btn9 = Button(layout, text="", width=10, height=6, command=lambda: handleBtnClick(9))


btn1.grid(row=0, column=0, padx=5, pady=5)
btn2.grid(row=0, column=1, padx=5, pady=5)
btn3.grid(row=0, column=2, padx=5, pady=5)
btn4.grid(row=1, column=0, padx=5, pady=5)
btn5.grid(row=1, column=1, padx=5, pady=5)
btn6.grid(row=1, column=2, padx=5, pady=5)
btn7.grid(row=2, column=0, padx=5, pady=5)
btn8.grid(row=2, column=1, padx=5, pady=5)
btn9.grid(row=2, column=2, padx=5, pady=5)


root.mainloop()
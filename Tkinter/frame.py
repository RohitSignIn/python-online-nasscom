from tkinter import *
root = Tk()

root.title("Frame")
root.geometry("800x600")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=5)
root.grid_rowconfigure(2, weight=1)


Header = Frame(root, background="red")
Header.grid(row=0, column=0, sticky="ewns")

Header.grid_columnconfigure(0, weight=1)

label1 = Label(Header, text="Header")
label1.grid(row=0, column=0)

MainFrame = Frame(root, background="green")
MainFrame.grid(row=1, column=0, sticky="ewns")

MainFrame.grid_columnconfigure(0, weight=1)
MainFrame.grid_columnconfigure(1, weight=2)

sideBar = Label(MainFrame, text="Sidebar", background="#2d2d2d")
sideBar.grid(row=0, column=0, sticky="ewns")

body = Label(MainFrame, text="Body", background="#454357")
body.grid(row=0, column=1, sticky="ewns")

Footer = Frame(root)
Footer.grid(row=2, column=0, sticky="ewns")

Footer.grid_columnconfigure(0, weight=1)

footerLabel = Label(Footer, text="Footer")
footerLabel.grid(row=0, column=0)



root.mainloop()
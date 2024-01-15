from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
root=Tk()
root.title("GAME")
moves=["stone","paper","scissors"]
# Shows the prompt for cpu button
 
def showpromptcpu():
    btnplayst=Button(root,text="STONE",padx=37,pady=20,bg="yellow",command=lambda:playbtnclick(btnplayst))
    btnplayst.grid(row=4,column=0)
 
    btnplaypap=Button(root,text="PAPER",padx=37,pady=20,bg="yellow",command=lambda:playbtnclick(btnplaypap))
    btnplaypap.grid(row=5,column=0)
 
    btnplaysic=Button(root,text="SCISSORS",padx=30,pady=20,bg="yellow",command=lambda:playbtnclick(btnplaysic))
    btnplaysic.grid(row=6,column=0)
 
    btnplay2st=Button(root,text="STONE",padx=37,pady=20,bg="yellow",command=lambda:playbtnclick(btnplay2st))
    btnplay2st.grid(row=4,column=4)
 
    btnplay2pap=Button(root,text="PAPER",padx=37,pady=20,bg="yellow",command=lambda:playbtnclick(btnplay2pap))
    btnplay2pap.grid(row=5,column=4)
 
    btnplay2sic=Button(root,text="SCISSORS",padx=30,pady=20,bg="yellow",command=lambda:playbtnclick(btnplay2sic))
    btnplay2sic.grid(row=6,column=4)
 
    labelresult=Label(root,text="RESULT",padx=30,pady=30,bg="lightgray")
    labelresult.grid(row=5,column=2)
 
    labelcpu=Label(root,text="YOU",padx=20,pady=20,bg="skyblue")
    labelcpu.grid(row=2,column=0)
 
    labelcpu2=Label(root,text="CPU",padx=20,pady=20,bg="skyblue")
    labelcpu2.grid(row=2,column=4)
 
# Handles cpu button click
 
def withcpuhandle():
    messagePrompt = " Start New Game ?"
 
    msg = messagebox.askquestion("start" ,messagePrompt)
    if(msg=="yes"):
        showpromptcpu()
 
# Handles images for player I
 
def playbtnclick(btn):
    print(btn, " Button clicked")
    if(btn=="stone"):
        img1=Image.open("C:/Users/LENOVO/Downloads/stone.jpg")
        im=ImageTk.PhotoImage(img1)
        Labelimg=Label(image=im,width=160,height=160,bg="pink")
        Labelimg.grid(row=5,column=1)
    elif(btn=="paper"):
        img2=Image.open("C:/Users/LENOVO/Downloads/paper.jpg")
        im=ImageTk.PhotoImage(img2)
        Labelimg=Label(image=im,width=160,height=160,bg="blue")
        Labelimg.grid(row=5,column=1)
    elif(btn=="scissors"):
        img3=Image.open("C:/Users/LENOVO/Downloads/scissors.jpg")
        im=ImageTk.PhotoImage(img3)
        Labelimg1=Label(image=im,width=160,height=160,bg="green")
        Labelimg1.grid(row=5,column=1)
 
# Shows prompt for player button click
 
def showpromptplay():
 
    btnplayst=Button(root,text="STONE",padx=37,pady=20,bg="yellow",command=lambda:playbtnclick(moves[0]))
    btnplayst.grid(row=4,column=0)
 
    btnplaypap=Button(root,text="PAPER",padx=37,pady=20,bg="yellow",command=lambda:playbtnclick(moves[1]))
    btnplaypap.grid(row=5,column=0)
 
    btnplaysic=Button(root,text="SCISSORS",padx=30,pady=20,bg="yellow",command=lambda:playbtnclick(moves[2]))
    btnplaysic.grid(row=6,column=0)
 
    btnplay2st=Button(root,text="STONE",padx=37,pady=20,bg="yellow")
    btnplay2st.grid(row=4,column=4)
 
    btnplay2pap=Button(root,text="PAPER",padx=37,pady=20,bg="yellow")
    btnplay2pap.grid(row=5,column=4)
 
    btnplay2sic=Button(root,text="SCISSORS",padx=30,pady=20,bg="yellow")
    btnplay2sic.grid(row=6,column=4)
 
    labelresult=Label(root,text="RESULT",padx=30,pady=30,bg="lightgray")
    labelresult.grid(row=5,column=2)
 
    labelcpu=Label(root,text="PLAYER I",padx=20,pady=20,bg="skyblue")
    labelcpu.grid(row=2,column=0)
 
    labelcpu2=Label(root,text="PLAYER II",padx=20,pady=20,bg="skyblue")
    labelcpu2.grid(row=2,column=4)
 
# Handles player button click
 
def withplayerhandle():
    messagePrompt = " Start New Game ?"
 
    msg = messagebox.askquestion("start" ,messagePrompt)
    if(msg=="yes"):
        showpromptplay()
 
 
 
 
label1=Label(root,text="PLAY WITH",padx=30,pady=30,bg="lightgreen")
label1.grid(row=0,column=2)
withcpu=Button(root,text=" CPU ",padx=10,pady=10,bg="skyblue",width=10,command=lambda:withcpuhandle())
withcpu.grid(row=1,column=1)
withplayer=Button(root,text=" PLAYER ",padx=10,pady=10,bg="skyblue",width=10,command=lambda:withplayerhandle())
withplayer.grid(row=1,column=3)
 
root.mainloop()
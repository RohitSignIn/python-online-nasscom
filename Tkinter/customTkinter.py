import customtkinter

app = customtkinter.CTk()

app.geometry("800x600")
app.title("First CustomtkInter")


btn = customtkinter.CTkButton(app, text="Button")
btn.grid(row=0, column=0)

btn = customtkinter.CTkEntry(app)
btn.grid(row=0, column=1)


app.mainloop()
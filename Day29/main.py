import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)


label1 = tkinter.Label(text="Website:", font=("Arial",10,"bold"))
label1.grid(column=0,row=1)

label1 = tkinter.Label(text="Email/Username:", font=("Arial",10,"bold"))
label1.grid(column=0,row=2)

label1 = tkinter.Label(text="Password:", font=("Arial",10,"bold"))
label1.grid(column=0,row=3)

button1 = tkinter.Button(text="Generate Password")
button1.grid(column=2, row=3)

button2 = tkinter.Button(text="Add")
button2.grid(column=1, row=4)

entry1 = tkinter.Entry(width= 35)
entry1.grid(column=1,row=1, columnspan=2)
entry2 = tkinter.Entry(width= 35)
entry2.grid(column=1,row=2, columnspan=2)
entry3 = tkinter.Entry(width= 21)
entry3.grid(column=1,row=3)

window.mainloop()
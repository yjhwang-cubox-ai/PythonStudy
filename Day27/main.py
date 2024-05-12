import tkinter

def click():
    mylabel.config(text=input.get())

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

mylabel = tkinter.Label(text="Hello", font=("Arial", 25))
mylabel.grid(column=0, row=0)

button = tkinter.Button(text="Button", command=click)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New_Button", command=click)
new_button.grid(column=2, row=0)

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
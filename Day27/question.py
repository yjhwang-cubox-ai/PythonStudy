import tkinter

def click():
    mile = input.get()
    killo = float(mile) * 1.61
    km.config(text=killo)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

mylabel1 = tkinter.Label(text="Miles", font=("Arial", 15))
mylabel1.grid(column=2, row=0)

mylabel2 = tkinter.Label(text="is equal to", font=("Arial", 15))
mylabel2.grid(column=0, row=1)

mylabel3 = tkinter.Label(text="km", font=("Arial", 15))
mylabel3.grid(column=2, row=1)

km = tkinter.Label(text="0", font=("Arial", 25))
km.grid(column=1, row=1)

button = tkinter.Button(text="Calculate", command=click, font=("Arial",10))
button.grid(column=1, row=2)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
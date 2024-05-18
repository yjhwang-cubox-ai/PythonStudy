import tkinter
import tkinter.constants
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(random.randint(8,10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2,4))]
    numbers_list = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = "".join(password_list[:10])
    
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_information():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any field anything!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"email: {email}\npassword: {password}\nIs OK?")
    
        if is_ok:
            with open("information.txt", mode="a", encoding="utf8") as file:
                file.write(f"{website} | {email} | {password}\n")
            print("saved!")
    
    website_entry.delete(0, tkinter.constants.END)
    password_entry.delete(0, tkinter.constants.END)
    

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)


label1 = tkinter.Label(text="Website:")
label1.grid(column=0,row=1)

label1 = tkinter.Label(text="Email/Username:")
label1.grid(column=0,row=2)

label1 = tkinter.Label(text="Password:")
label1.grid(column=0,row=3)

gen_pw_button = tkinter.Button(text="Generate Password", command=generate_password)
gen_pw_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=44, command=save_information)
add_button.grid(column=1, row=4, columnspan=2)

website_entry = tkinter.Entry(width= 44)
website_entry.grid(column=1,row=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width= 44)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0, "aaa@aa.com")
password_entry = tkinter.Entry(width= 28)
password_entry.grid(column=1,row=3)

window.mainloop()
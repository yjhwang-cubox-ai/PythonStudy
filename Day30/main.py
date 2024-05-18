import tkinter
import tkinter.constants
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    try:
        with open("data.json", "r", encoding="utf8") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="There are not password information!")
    else:        
        search_website = website_entry.get().upper()
        if search_website in data:
            search_password = data[search_website]['password']
            search_email = data[search_website]['email']
            messagebox.showinfo(message=f"{search_website}\nEmail: {search_email}\nPassword: {search_password}")
        else:
            messagebox.showinfo(message="There are not that site's password!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [random.choice(letters) for _ in range(random.randint(8,10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2,4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2,4))]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = "".join(password_list[:10])
    
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_information():
    website = website_entry.get().upper()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }
    
    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any field anything!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"email: {email}\npassword: {password}\nIs OK?")
    
        if is_ok:
            try:
                with open("data.json", "r", encoding="utf8") as file:
                    data = json.load(file)                    
            except FileNotFoundError:
                with open("data.json", "w", encoding="utf8") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)        
                with open("data.json", "w", encoding="utf8") as file:
                    json.dump(data, file, indent=4)
                print("saved!")
            finally:
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

search_button = tkinter.Button(text="Search", command=search, width=13)
search_button.grid(column=2, row=1)

gen_pw_button = tkinter.Button(text="Generate Password", command=generate_password)
gen_pw_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=44, command=save_information)
add_button.grid(column=1, row=4, columnspan=2)

website_entry = tkinter.Entry(width= 28)
website_entry.grid(column=1,row=1)
website_entry.focus()
email_entry = tkinter.Entry(width= 44)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0, "aaa@aa.com")
password_entry = tkinter.Entry(width= 28)
password_entry.grid(column=1,row=3)

window.mainloop()
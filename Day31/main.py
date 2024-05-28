import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

words = pd.read_csv('Day31/data/french_words.csv')

content = words.to_dict(orient="records")

def inverse_card(en_text):
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(content_text, text=en_text)
    canvas.itemconfig(canvas_image, image=card_back_img)

def change_word():
    french_word = random.choice(content)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(content_text, text=french_word['French'])
    canvas.itemconfig(canvas_image, image=card_front_img)
    en_text = french_word['English']

    window.after(3000, inverse_card, en_text)
    

window = tkinter.Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file='Day31/images/card_front.png')
card_back_img = tkinter.PhotoImage(file='Day31/images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
content_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))

x_img = tkinter.PhotoImage(file='Day31/images/wrong.png')
button_x = tkinter.Button(image=x_img, highlightthickness=0, command=change_word)
button_x.grid(column=0, row=1)

v_img = tkinter.PhotoImage(file='Day31/images/right.png')
button_v = tkinter.Button(image=v_img, highlightthickness=0, command=change_word)
button_v.grid(column=1, row=1)

tkinter.mainloop()
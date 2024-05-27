import tkinter
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

words = pd.read_csv('flash-card-project-start\\data\\french_words.csv')

content = words.to_dict(orient="records")

def change_word():
    

window = tkinter.Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = tkinter.PhotoImage(file='flash-card-project-start\\images\\card_front.png', )
canvas.create_image(400,263,image=card_img)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
content_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))

x_img = tkinter.PhotoImage(file='flash-card-project-start\\images\\wrong.png')
button_x = tkinter.Button(image=x_img, highlightthickness=0, command=)
button_x.grid(column=0, row=1)

v_img = tkinter.PhotoImage(file='flash-card-project-start\\images\\right.png')
button_v = tkinter.Button(image=v_img, highlightthickness=0, command=)
button_v.grid(column=1, row=1)

tkinter.mainloop()
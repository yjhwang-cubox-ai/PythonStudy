from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_label.config(text='')
    global REPS
    REPS = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    
    work_sec = WORK_MIN * 5
    short_break_sec = SHORT_BREAK_MIN * 3
    long_break_sec = LONG_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
        
    if REPS % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        
    if REPS % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        
    
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # print("count_down")
    #"00:00"
    minute = math.floor(count / 60)
    sencond = int(count % 60)
    
    updated_count_text = f"{minute:02}:{sencond:02}"
    
    canvas.itemconfig(timer_text, text=updated_count_text)
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        global REPS
        for _ in range(math.floor(REPS/2)):
            mark += '✔'
        check_label.config(text=mark)
            

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# window.minsize(width=500, height=500)
window.config(padx=70, pady=30, bg=YELLOW)

#label
title_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

#image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#button
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

#check
check_label = Label(font=(15),fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
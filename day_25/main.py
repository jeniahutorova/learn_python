from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global timer

    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1

    if reps % 8 == 0 :
        time = LONG_BREAK_MIN
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        time = SHORT_BREAK_MIN
        label.config(text="Break", fg=PINK)
    else:
        time = WORK_MIN
        label.config(text="Work", fg=GREEN)
    
    time_converted = time * 60
    count_down(time_converted)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10: 
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            checkmark.config(text="✓")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file=r"C:\Users\jenia\Desktop\learn_python\day_25\tomato.png")

canvas = Canvas(width=200, height=240, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

label = Label(window, text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
label.grid(column=2, row=1)

start_button = Button(window, text="Start", font=(FONT_NAME, 10), command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(window, text="Reset", font=(FONT_NAME, 10), command=reset_timer)
reset_button.grid(column=3, row=3)

checkmark = Label(window, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20) )
checkmark.grid(column=2, row=4)

window.mainloop()
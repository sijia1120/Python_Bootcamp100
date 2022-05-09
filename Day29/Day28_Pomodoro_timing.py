
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5#5
LONG_BREAK_MIN = 3#20
repc = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    time_label.config(text="My tomato")
    check_mark.config(text="")
    global repc
    repc = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repc
    repc += 1

    if repc == 9:
        count_down(0)
    elif repc % 8==0:
        count_down(LONG_BREAK_MIN*60)
        time_label.config(text="Long Break",fg= RED)
    elif repc % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        time_label.config(text="Short Break", fg =PINK)
    else:
        count_down(WORK_MIN*60)
        time_label.config(text="Work",fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # 00:00
    count_min = math.floor(count/60)
    count_sec =count % 60
    mark =""

    if count_sec<10:
        count_sec = f"0{count_sec}"

    if count_min <10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        print(count)
        global timer
        timer = window.after(1000, count_down, count-1 )
    else:
        start_timer()
        work_cycle = math.ceil(repc / 2)
        print(work_cycle)
        for cycle in range(work_cycle):
            mark += "✔"
        check_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW )

canvas = Canvas(width= 200, height=224, bg= YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= tomato_image)
timer_text = canvas.create_text(100,130, text= "00:00",fill= "white", font=(FONT_NAME,35,"bold"))
canvas.grid(column = 1, row = 1)


time_label = Label(text= "Timer",fg=GREEN,bg=YELLOW, font=(FONT_NAME,45,"bold"))
time_label.grid(column = 1, row = 0)

# Button
start_button =Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset" , bg=YELLOW, highlightthickness=0, command = reset_timer)
reset_button.grid(column=2, row=2)
# checkbar
check_mark = Label(fg=GREEN, bg= YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()

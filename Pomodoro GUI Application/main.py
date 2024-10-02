from idlelib.colorizer import color_config
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bd999"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    reps += 1
    if reps%2==1:
        my_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps==8:
        my_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps%2==0:
        my_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    check = ''
    for i in range(reps // 2):
        check = check + '✓'
    checkmark.config(text=check)

# ---------------------------- COUNTDOWN MECHANISM -------------------------------
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec="0"+str(count_sec)
    if count_min<10:
        count_min="0"+str(count_min)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000, count_down,count-1)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas=Canvas(window, width=200, height=223, bg=YELLOW, highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text=canvas.create_text(101,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"),anchor=CENTER)
canvas.pack()
canvas.grid(column=1,row=1)

my_label=Label(window, text='Timer',font=(FONT_NAME,40,"bold"),bg=YELLOW, fg=GREEN)
my_label.grid(column=1, row=0)

button1=Button(text="Start",font=(FONT_NAME,15,"bold"), bg=GREEN,fg="white",command=start_timer)
button1.grid(column=0, row=2)

button2=Button(text="Reset",font=(FONT_NAME,15,"bold"), bg=GREEN,fg="white", command=reset_timer)
button2.grid(column=2, row=2)

checkmark=Label(window, text='',font=(FONT_NAME,15,"bold"),bg=YELLOW, fg=GREEN, highlightthickness=0)
checkmark.grid(column=1, row=3)

window.mainloop()
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
counter=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    Timer_Label.configure(text="Timer")
    window.after_cancel(timer)
    canvas.itemconfig(timer_dec,text="00:00")
    check_mark.configure(text="")
    global counter
    counter=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global counter
    counter+=1
    if counter%8==0:
            Timer_Label.configure(text="20 Min Break",foreground=RED)
            count_down(LONG_BREAK_MIN*60)
    elif counter%2==0:
        Timer_Label.configure(text="05 Min Break",foreground=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        Timer_Label.configure(text="Study",foreground=GREEN)
        count_down(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count>=0:
        global timer
        min=math.floor(count/60)
        sec=count%60
        if sec<10:
            sec=f"0{sec}"
        if min<10:
            min=f"0{min}"
        canvas.itemconfig(timer_dec, text=f"{min}:{sec}")
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        for _ in range(0,math.floor(counter/2)):
            mark+="✅"
        check_mark.configure(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
# window.minsize(width=800, height=600)
window.configure(padx=200,pady=100)
window.configure(background=YELLOW)
Timer_Label = Label(font=(FONT_NAME,50,"bold"),text="Timer",foreground=GREEN,background=YELLOW)
Timer_Label.grid(row=0,column=1)
image_src= PhotoImage(file="tomato.png")
canvas = Canvas(width=500, height=400,highlightthickness=0, background=YELLOW,bg=YELLOW)
canvas.create_image(250,200,image=image_src)
timer_dec = canvas.create_text(250,225,text="00:00",fill=YELLOW,font=(FONT_NAME,25,"bold"))
canvas.grid(row=1,column=1)
window.title("Pomodoro Technique")
button_start= Button(text="Start",highlightthickness=0,background=YELLOW,font=(FONT_NAME,20,"bold"),command=start_timer)
button_start.grid(row=2,column=0)
button_reset= Button(text="Reset",highlightthickness=0,background=YELLOW,font=(FONT_NAME,20,"bold"),command=reset_timer)
button_reset.grid(row=2,column=2)
check_mark=Label(background=YELLOW,font=(FONT_NAME,15,"bold"))
check_mark.grid(row=2,column=1)
window.mainloop()
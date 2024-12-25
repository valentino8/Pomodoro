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
    window.after_cancel(timer)
    timer_label.config(text = "Timer",fg = GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text= "")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN*60

    timer_on = True
    reps += 1

    if reps%2 != 0 :
        count_down(work_sec)
        timer_label.config( text = "Work Session",fg = RED)

    elif reps%2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)

    elif reps%8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=PINK)






# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    if count_min <= 9:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text =f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark =""
        for _ in range(math.floor(reps/2)):
            mark+= "✔️"
        check_mark.config(text = mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Poomodoro")
window.config(padx = 100,pady = 100,bg=YELLOW)

timer_label = Label(text="Timer",font = ("sans seriff",35,"italic"))
timer_label.config(fg = GREEN,bg = YELLOW)
timer_label.grid(column = 1,row= 0)


canvas = Canvas(width = 300, height=300,bg = YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(160,130,image = tomato_img)
timer_text = canvas.create_text(160,160,text = "00:00",fill="white",font = (FONT_NAME,24,"bold"))
canvas.grid(column = 1,row = 1)
check_mark = Label(fg="green",bg= YELLOW,font=(FONT_NAME,24,"bold"))
check_mark.grid(column = 1,row =3)

# def motion(event):
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))
#
# window.bind('<Motion>', motion)


start_button = Button(window,text = "Start",font = ("sans seriff",10,"italic"),height=2,width = 10,cursor="hand2",command = start_timer)
start_button.place(x=-50, y=290)

reset_button = Button(window,text = "Reset",font = ("sans seriff",10,"italic"),height=2,width = 10,cursor="hand2",command=reset_timer)
reset_button.place(x=290, y=290)

window.mainloop()
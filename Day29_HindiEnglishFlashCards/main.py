from tkinter import *
import pandas,random
Background_color = "#b1ddc6"
with open("./Data/Hindi_Words.csv", newline='', encoding='utf-8') as file:
    data = pandas.read_csv(file)
    to_learn = data.to_dict('records')
    words={}
def button_clicked():
    global words,flip_timer
    window.after_cancel(flip_timer)
    words= random.choice(to_learn)
    canvas.itemconfig(title_pro, text="Hindi",fill="Black")
    canvas.itemconfig(word_pro,text=words['Hindi Word'],fill="Black")
    canvas.itemconfig(image_appear,image=front_img)
    flip_timer = window.after(3000,change_card)
def not_known():
        with open("Data/not_known_words.txt", "a", encoding='utf-8') as file:
            file.write(f"{words['Hindi Word']}--------->{words['English Word']}\n\n")
        button_clicked()
def change_card():
    canvas.itemconfig(image_appear,image=back_img)
    canvas.itemconfig(title_pro, text="English",fill="white")
    canvas.itemconfig(word_pro, text=words['English Word'],fill="white")
def remove_word():
    to_learn.remove(words)
    button_clicked()
window=Tk()
window.title("Flash Card")
window.config(background=Background_color)
window.config(padx=50,pady=50)
flip_timer= window.after(3000,change_card)
front_img = PhotoImage(file="./images/card_front.png")
back_img= PhotoImage(file="./images/card_back.png")
canvas = Canvas(width= 800 ,height = 526,highlightthickness=0,bg=Background_color)
image_appear = canvas.create_image(400,263,image=front_img)
canvas.grid(row=1,column=0,columnspan=3)
title_pro=canvas.create_text(400,150,text="",font=("Arial",40,"bold"))
word_pro=canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
not_known_img = PhotoImage(file="./images/wrong.png")
not_known_btn = Button(image=not_known_img,highlightthickness=0,command=not_known)
known_img = PhotoImage(file="./images/right.png")
known_btn = Button(image=known_img,highlightthickness=0,command=remove_word)
not_known_btn.grid(row=2,column=0)
known_btn.grid(row=2,column=2)
button_clicked()
window.mainloop()

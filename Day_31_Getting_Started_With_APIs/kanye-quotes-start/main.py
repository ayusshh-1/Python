from tkinter import *
import requests

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    quote = response.json()["quote"]
    canvas.itemconfig(text_quote,text=quote)

window = Tk()
window.title("Kanye")
window.config(padx=50, pady=50)
canvas= Canvas(width = 300  ,  height = 414)
imag_back = PhotoImage(file="background.png")
canvas.create_image(150,207,image=imag_back)
text_quote = canvas.create_text(150,207,text="",width=250, fill="black",font=("Arial",20,"bold"))
canvas.grid(row=1,column=1)
image_kanye = PhotoImage(file="kanye.png")
press_button= Button(image=image_kanye, command=get_quote)
press_button.grid(row=2,column=1)


window.mainloop()
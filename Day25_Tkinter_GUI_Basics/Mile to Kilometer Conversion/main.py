from tkinter import *
window=Tk()
window.title("Mile to Kilometer")
window.config(padx=100, pady=100)

input = Entry(width=7)
input.grid(row=0,column=1)

label= Label(text="Miles")
label.grid(row=0,column=2)

label1= Label(text="is Equal to ")
label1.grid(row=1,column=0)

label2 = Label(text="0")
label2.grid(row=1,column =1)

label3= Label(text="Km")
label3.grid(row=1,column=2)

def conversion():
    miles = float(input.get())
    km = miles * 1.60934
    label2.config(text=f"{km}")
button = Button(text="Calculate",command=conversion)
button.grid(row=2,column=1)

window.minsize(200,200)
window.mainloop()

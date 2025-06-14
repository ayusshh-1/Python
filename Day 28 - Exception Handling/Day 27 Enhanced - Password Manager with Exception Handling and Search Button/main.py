from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
from json.decoder import JSONDecodeError
counter=0
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [letters[letter] for letter in range(nr_letters)]
    password_symbol=[symbols[symbol] for symbol in range(nr_symbols)]
    password_number = [numbers[num] for num in range(nr_numbers)]
    password_list=password_letter+password_symbol+password_number
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    global counter
    counter+=1
    website_data= website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    json_format = { website_data:{"email":email_data,"password":password_data}}
    if website_data == "" or email_data == "" or password_data == "":
        empty = messagebox.showerror("Error", "Please fill all fields")
    else:
        check = messagebox.askokcancel(title="Save the Details" , message= f"Are u sure u want to save these details ? \n Website: {website_data} \n Email: {email_data} \n Password: {password_data}")
        if check :
            try:
                with open("data.json","r") as data:
                    data_file = json.load(data)
            except (FileNotFoundError,JSONDecodeError):
                with open("data.json","w") as data:
                    json.dump(json_format,data,indent=4)
            else:
                data_file.update(json_format)
                with open("data.json","w") as d_file:
                    json.dump(data_file,d_file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            pass
# ---------------------------- Check Password ------------------------------- #
def search_website():
    website = website_entry.get()
    try:
        with open("data.json","r") as show:
            data = json.load(show)
    except FileNotFoundError:
           messagebox.showinfo("Error","Data Not found")
    else:
            if website in data:
                    email_got = data[website]['email']
                    password_fetch = data[website]['password']
                    messagebox.showinfo(title=f"{website}", message=f"Your ID is {email_got}\n Your Password is {password_fetch}")
            else:
                messagebox.showerror(title="Error Message",message="Data Not found")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(padx=40,pady=40)
#adding image
canvas = Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

#labels
website = Label(text="Website")
website.grid(row=1,column=0)
email = Label(text="Email/Username")
email.grid(row=2,column=0)
password= Label(text="Password")
password.grid(row=3,column=0)


#entries
website_entry =Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry =Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"phoenixits29@gmail.com")
password_entry =Entry(width=21)
password_entry.grid(row=3,column=1)

# button
search_btn=Button(text="Search",command=search_website)
search_btn.grid(row=1,column=2)
password_gene = Button(text="Generate Password",width=14,command=generate_password)
password_gene.grid(row=3,column=2)
add_pass = Button(text="Add Password",width=36,command=add)
add_pass.grid(row=4,column=1,columnspan=2)
window.title("Password Manager")
window.mainloop()


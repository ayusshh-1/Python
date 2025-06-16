import smtplib
import datetime as dt
import pandas as pd
import random
from email.message import EmailMessage

# ---------------------- Configuration ---------------------- #
my_email = "your_email"
my_password = "cyour_app_password"
letter_files = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# ---------------------- Get Today's Date ---------------------- #
now = dt.datetime.now()
todays_day = now.day
todays_month = now.month

# ---------------------- Read Birthdays ---------------------- #
data = pd.read_csv("birthdays.csv")
dob_person = data[(data['day'] == todays_day) & (data['month'] == todays_month)]

if not dob_person.empty:
    dob_name = dob_person['name'].iloc[0]
    dob_email = dob_person['email'].iloc[0]

    # ---------------------- Prepare Birthday Letter ---------------------- #
    chosen_letter = random.choice(letter_files)
    with open(f"./letter_templates/{chosen_letter}", "r", encoding="utf-8") as file:
        content = file.read()
        personalized_message = content.replace("[Name]", dob_name)

    # ---------------------- Create Email ---------------------- #
    msg = EmailMessage()
    msg["Subject"] = "🎂 Birthday Wishes From your_name 🎉"
    msg["From"] = my_email
    msg["To"] = dob_email
    msg.set_content(personalized_message)

    # ---------------------- Send Email ---------------------- #
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.send_message(msg)

    print(f"Email sent to {dob_email}")
else:
    print("No birthdays today.")

🎉 Automated Birthday Email Wisher
A Python project that automatically sends personalized birthday wishes via email using a set of pre-written templates. Useful for automating greetings and never missing someone’s special day.

✨ Features
Reads birthday data from a CSV file

Checks daily for any birthdays matching today’s date

Sends a customized email with the recipient's name

Chooses a random birthday message template

Uses Gmail SMTP for sending emails

Deployable on a cloud server like PythonAnywhere

📁 Project Structure
📦 birthday-wisher
┣ 📜 main.py

┣ 📄 birthdays.csv

┣ 📂 letter_templates/

┃ ┣ 📄 letter_1.txt

┃ ┣ 📄 letter_2.txt

┃ ┗ 📄 letter_3.txt

📝 How to Use
1. Setup Gmail
Enable 2-Step Verification in your Gmail account.

Create an App Password for Gmail.

Replace my_email and my_password in the script with your email and app password.

2. Add Birthdays
Update birthdays.csv file with entries in this format:
name,email,year,month,day
📝 Make sure there's no extra space and file is saved in UTF-8.

☁️ Deploy on PythonAnywhere
Step-by-step Instructions:
Sign up or log in at https://www.pythonanywhere.com

Go to Files, upload your project folder (main.py, birthdays.csv, letter_templates/)

Open the Console, and run:
python3 main.py
To automate daily sending:

Go to Tasks in the dashboard

Schedule a daily task:
python3 /home/your_username/main.py

✅ Requirements
Python 3.6+

Packages used:

smtplib

datetime

pandas

random

email.message

📌 Notes
You must manually add birthday entries to birthdays.csv for recipients.

The script only sends one email per day, even if multiple people share the same birthday.

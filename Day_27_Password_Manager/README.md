# 🔐 Password Manager

A simple password manager built using Python's Tkinter library. This app allows you to generate secure passwords, copy them to your clipboard, and save login information (website, email/username, password) locally in a text file.

---

## 📌 Features

- 🎲 Secure password generation (letters, numbers, symbols)
- 📋 Automatically copies generated password to clipboard
- 💾 Save website/email/password to `data.txt`
- 🔐 Confirmation prompt before saving
- 🖥️ Graphical User Interface using Tkinter

---

## 📦 Requirements

- Python 3.x
- [`pyperclip`](https://pypi.org/project/pyperclip/) library

Install pyperclip with:

```bash
python -m pip install pyperclip

▶️ How to Run
1. Clone or download this repository.
2. Ensure the following files are in the same directory:
   password_manager.py
   logo.png (your app icon/logo)
3. Run the script:
   python password_manager.py
💡 How It Works
Click "Generate Password" to generate a secure password. It is auto-copied to your clipboard.

Fill in the website and email/username fields.

Click "Add Password" to save the entry to data.txt. A confirmation dialog will appear before saving.

Example output in data.txt:
1  Website: github.com | Email: example@gmail.com | Password: D3!e7$Km

🖼️ GUI Layout
+-------------------------------+
|           [Logo]             |
|-----------------------------|
| Website:       [         ]   |
| Email/User:    [         ]   |
| Password:      [       ] [Generate] |
|                             |
|        [Add Password]       |
+-------------------------------+

📁 File Structure
password_manager/
│
├── password_manager.py
├── logo.png
└── data.txt  ← (auto-created after saving data)
🚀 Future Enhancements (Ideas)
Encrypt saved passwords for security

Add search/filter functionality

Use SQLite or JSON instead of .txt

Add dark mode support

🙋 Author
Developed by AYUSH R YADAV

Feel free to customize, contribute, or reach out!

⚠️ Disclaimer
This tool is for educational/demo purposes only. Do not use it for storing real credentials without implementing proper security and encryption.

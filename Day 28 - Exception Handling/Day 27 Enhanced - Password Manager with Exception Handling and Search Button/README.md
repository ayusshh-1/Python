🔐 Password Manager with Exception Handling & Search Feature
This is an enhanced version of the Day 27 Password Manager created as part of my 100 Days of Code challenge. On Day 28, I implemented exception handling and added a search functionality to read from the saved credentials stored in a JSON file.

✅ Features
Save website login credentials (email & password)

Data stored in data.json using JSON format

Generate strong random passwords

Copy password to clipboard automatically

NEW: Search functionality to retrieve saved credentials by website

NEW: Exception handling to avoid app crashes (e.g., missing file, empty JSON)

💡 Enhancements Made
Feature            	Description
🔍 Search Button:- Lets you look up saved email & password for a given website.
❗ Exception Handling:-	Prevents crashes if the JSON file doesn't exist or is empty. Uses try, except, else, and finally.
📄 Data Persistence	Data:- is updated/appended in data.json using json.load() and json.dump() safely.

📦 Technologies Used
Python 3

tkinter (GUI)

json (for file handling)

random & string (for password generation)

pyperclip (to copy password to clipboard)

Day 27 Enhanced - Password Manager with Exception Handling/
│
├── main.py              # Main application file with GUI
├── data.json            # JSON file to store saved credentials
├── README.md            # This file

🧠 What I Learned
How to handle file-related and JSON decoding exceptions gracefully

How to read from and update JSON files dynamically

How to structure GUI-based features to improve user experience


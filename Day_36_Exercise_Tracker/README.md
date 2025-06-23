# 🚀 Day 36 – Exercise Tracker with Nutritionix & Sheety API

Welcome to Day 36 of my #100DaysOfCode journey!  
Today, I built an **Exercise Tracker** using two APIs:

- 🥗 **Nutritionix API**: To analyze exercise text input and return calories, duration, etc.
- 📊 **Sheety API**: To log the exercise data into a Google Sheet via REST API.

---

## 📌 Features

✅ Takes natural language input (e.g., "ran 2 km and cycled 10 minutes")  
✅ Sends input to the Nutritionix API to get calorie data  
✅ Logs the exercise data (name, duration, calories, date & time) into a Google Sheet  
✅ Uses environment variables to securely store API keys

---

## 🧠 Concepts Practiced

- Working with **external APIs**
- Handling **HTTP POST requests** with `requests`
- Managing **environment variables** using `.env` and PyCharm config
- Parsing JSON responses
- Using `datetime` for date and time formatting

---

## ⚙️ Requirements

- Python 3.7+
- `requests` library
- `python-dotenv` (if using `.env` file)

Install dependencies:

```bash
pip install requests python-dotenv

🔐 Environment Variables
Set these in .env or in your IDE (e.g., PyCharm run configurations):
API_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_app_key
SHEET_ENDPOINT=https://api.sheety.co/your_endpoint
SHEET_NAME=workout
TOKEN=Bearer your_token

🏁 How to Run
python main.py
You'll be prompted to enter what exercise you did. Examplpe:
Tell which exercise you did: ran 2 km and did 10 min yoga

The script will:

Parse your input and fetch calorie & duration data from Nutritionix

Format and send it to your Google Sheet via Sheety

Print the API response
📸 Sample Output
{
  "workout": {
    "date": "23/06/2025",
    "time": "11:00:21",
    "exercise": "Running",
    "duration": 15.2,
    "calorie": 123.4
  }
}
🔚 Summary
This project was a great practice in integrating multiple APIs, working with JSON data, and managing secret keys securely.
👨‍💻 Day 36 Completed ✅


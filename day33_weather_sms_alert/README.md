# 🌧️ Weather Alert via SMS – Day 33

This project fetches the weather forecast from the **OpenWeatherMap API** and sends an SMS alert using **Twilio** if rain is expected in the next 12 hours. This was part of my **Day 33** of the #100DaysOfCode challenge.
## 🧠 What I Learned

- Using the **OpenWeatherMap API** to gather 3-hour interval forecast data.
- Detecting upcoming rain using weather condition codes (`weather_id`).
- Sending SMS alerts with **Twilio's Python SDK**.
- The importance of using **environment variables** to securely manage sensitive credentials.

---
## 📦 Dependencies

- `requests` – for making HTTP API calls.
- `twilio` – for sending SMS.
- Python 3.6 or higher.

Install dependencies:
```bash
pip install requests twilio

🧾 How It Works
Calls OpenWeatherMap's forecast API with your location (latitude & longitude).

Checks the next 4 forecast entries (covering the next 12 hours).

If any forecast shows a weather ID below 700 (rain/snow), it sends a rain alert via SMS.

Uses Twilio API to send the message to your verified phone number.

📬 Sample SMS Output
It is going to be rain ⛈️ don't forget to bring Umbrella ☂️

🧪 Sample Output (Console)
500
queued

📍 Example API URL

https://api.openweathermap.org/data/2.5/forecast?lat=23.014509&lon=72.591759&appid=YOUR_API_KEY
🙌 Credits
OpenWeatherMap API

Twilio Python Library

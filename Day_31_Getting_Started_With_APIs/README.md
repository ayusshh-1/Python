# 📦 Day 31 – Exploring APIs with Python

On Day 31 of my **#100DaysOfCode** challenge, I worked with **APIs** using Python and created three small but meaningful projects. Each one uses a different public API to demonstrate how to fetch data, parse responses, and build something useful or fun.

---

## 📁 Folder Structure
Day 33 API/
├── ISS_Tracker_With_Email/ # ISS position + email alert if overhead during night
│ └── main.py
│
├── kanye-quotes-start/ # GUI app to fetch random Kanye West quotes
│ ├── background.png
│ ├── kanye.png
│ └── main.py
│
└── Sunrise_Sunset_Time/ # Fetches sunrise and sunset data for a location
|   |── main.py


---

## 🌌 1. ISS Tracker With Email Notification

**Folder**: `ISS_Tracker_With_Email/`

- Uses the **Open Notify API** to get real-time ISS location.
- Uses the **Sunrise-Sunset API** to determine if it’s dark.
- Sends an **email alert** if the ISS is overhead **and** it’s nighttime.

🔗 APIs Used:
- [ISS Location API](http://api.open-notify.org/iss-now.json)
- [Sunrise-Sunset API](https://sunrise-sunset.org/api)

📧 Email sent using `smtplib` with SMTP (Gmail).

---

## 🎤 2. Kanye Quotes GUI App

**Folder**: `kanye-quotes-start/`

- Uses the [Kanye Rest API](https://api.kanye.rest) to fetch random Kanye West quotes.
- Built with **Tkinter** for a fun click-and-refresh interface.
- Shows a quote over a styled background and image of Kanye.

📚 Concepts:
- GUI development with Tkinter
- API call on button click
- Updating widgets dynamically

---

## 🌅 3. Sunrise & Sunset Time Fetcher

**Folder**: `Sunrise_Sunset_Time/`

- Fetches **sunrise** and **sunset** times for a given latitude & longitude.
- Uses the [Sunrise-Sunset API](https://sunrise-sunset.org/api)
- Helps understand how location and time zones affect daylight hours.

📌 Location used: Ahmedabad, Gujarat (India)

---

## 🔧 Skills Practiced

- Making `GET` requests using the `requests` module
- Working with JSON data in Python
- Basic GUI development with `tkinter`
- Email automation via `smtplib`
- Handling geographic and time-based data

---

## ✅ Summary

Day 31 helped me understand how powerful APIs are, even when used with simple Python tools. Whether it’s real-time satellite data, fun quotes, or time calculations, APIs can turn code into something truly interactive.

> 🚀 On to the next challenge!



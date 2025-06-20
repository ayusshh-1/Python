Day 34 - Stock Price Alert & News Notifier 📈📱

🗓️ Day 34 of 100 Days of Code
Today, I built a Python script that:

Monitors daily stock prices of Tesla (TSLA).

Checks for a price change >±5% between days.

If the threshold is crossed, fetches the latest news articles about the company.

Notifies you via Twilio SMS.
🚀 Features
✅ Pulls daily stock prices using the Alpha Vantage API.

✅ Determines significant price changes (±5%) from the prior trading day.

✅ Gets the top 3 latest news articles about the company from the News API.

✅ Sends an SMS alert via Twilio with relevant headline, description, and trend icon (🔝 or 🔻).

⚡️ Tech Stack
Python 3.9+

requests for making API calls

twilio for sending SMS

datetime for date calculations

🔥 How It Works
The script fetches:

Yesterday’s and the prior day’s stock prices.

Latest news articles about the stock.

Determines if the stock price increased or decreased by ≥5%.

If condition met, sends an SMS alert with:

Direction of the trend (🔝 / 🔻).

News headline.

⚙️ Setup Instructions

Clone this Repository:
git clone https://github.com/<yourusername>/100DaysOfCode.git
cd Day_34_Stock_Alert

Install Dependencies:
pip install requests twilio

Add API Keys:

Get your Alpha Vantage API Key: https://www.alphavantage.co/

Get your News API Key: https://newsapi.org/

Get your Twilio Account Sid and Auth Token: https://www.twilio.com/

Replace the placeholders in the script:
MY_STOCK_API = "<your_alpha_vantage_api_key>"
MY_NEWS_API = "<your_news_api_key>"
account_sid = "<your_twilio_account_sid>"
auth_token = "<your_twilio_auth_token>"
twilio_number = "<your_twilio_phone_number>"
to_number = "<your_phone_number>"

Run the Script:
python stock_alert.py

🙌 Acknowledgments
Alpha Vantage for stock data.

News API for news data.

Twilio for making SMS alerts possible.



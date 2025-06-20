import requests
import datetime
from twilio.rest import Client

# --------------------------------------------------
# 👉 ENTER YOUR CREDENTIALS BELOW
# --------------------------------------------------
MY_NEWS_API = "your_news_api_here"
MY_STOCK_API = "your_stock_api_here"

ACCOUNT_SID = "your_account_sid_here"
AUTH_TOKEN = "your_auth_token_here"
TWILIO_NUMBER = "your_twilio_number_here"
TO_NUMBER = "your_destination_number_here"

STOCK_NAME = "TSLA"

# --------------------------------------------------
# CALCULATING RELEVANT DATES
# --------------------------------------------------
now = datetime.datetime.now()
from_dt = now.date()
yesterday_stock = from_dt - datetime.timedelta(days=2)
day_b_yesterday_stock = from_dt - datetime.timedelta(days=3)

yesterday_news = from_dt - datetime.timedelta(days=1)
day_b_yesterday_news = from_dt - datetime.timedelta(days=2)

# --------------------------------------------------
# FETCH STOCK PRICES
# --------------------------------------------------
stock_parameters = {
    "apikey": MY_STOCK_API,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME
}
responces = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)

yesterday_close_price = float(responces.json()["Time Series (Daily)"][f"{yesterday_stock}"]["4. close"])
day_b_yesterday_close_price = float(responces.json()["Time Series (Daily)"][f"{day_b_yesterday_stock}"]["4. close"])

# --------------------------------------------------
# FETCH RELEVANT NEWS
# --------------------------------------------------
def news():
    news_parameter = {
        "apiKey": MY_NEWS_API,
        "q": "TSLA",
        "searchIn": {
            "title": "Tesla"
        },
        "sortBy": "relevancy, popularity, publishedAt",
        "source": "bloomberg.com, cnbc.com, reuters.com, marketwatch.com, wsj.com",
        "from": day_b_yesterday_news,
        "to": yesterday_news,
        "language": "en"
    }
    responses = requests.get(url="https://newsapi.org/v2/everything", params=news_parameter)
    articles = responses.json()["articles"]
    three_article = articles[:3]
    return three_article

# --------------------------------------------------
# CALCULATE THRESHOLDS
# --------------------------------------------------
inc_5 = day_b_yesterday_close_price * 1.05
dec_5 = day_b_yesterday_close_price * 0.95

# --------------------------------------------------
# SEND SMS IF THRESHOLDS ARE MET
# --------------------------------------------------
client = Client(ACCOUNT_SID, AUTH_TOKEN)

if yesterday_close_price >= inc_5 or yesterday_close_price <= dec_5:
    get_news = news()
    for article in get_news:
        if yesterday_close_price >= inc_5:
            symbol_show = "🔻"
        else:
            symbol_show = "🔝"

        message = client.messages.create(
            body=f"Stock {STOCK_NAME} has been {symbol_show} \n {article}",
            from_=TWILIO_NUMBER,
            to=TO_NUMBER
        )
        print(message.status)


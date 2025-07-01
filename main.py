import requests
from twilio.rest import Client
import time
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
MAX_SMS_LENGTH = 150

# Load sensitive credentials from environment variables
Alphavantage_API_Key = os.getenv("ALPHAVANTAGE_API_KEY")
News_API_Key = os.getenv("NEWS_API_KEY")
Twilio_Account_SID = os.getenv("TWILIO_ACCOUNT_SID")
Twilio_Auth_Token = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")

client = Client(Twilio_Account_SID, Twilio_Auth_Token)

News_API_Parameters = {
    "q": COMPANY_NAME,
    "apiKey": News_API_Key,
    "pageSize": 3,
}

Alphavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": Alphavantage_API_Key
}

response = requests.get("https://www.alphavantage.co/query", params=Alphavantage_parameters)
response.raise_for_status()
print(response.status_code)

data = response.json()
time_series = data.get("Time Series (Daily)")

if not time_series:
    print("Time series data unavailable.")
    exit()

dates = list(time_series.keys())
yesterday = time_series[dates[0]]
day_before_yesterday = time_series[dates[1]]

yesterday_close = float(yesterday["4. close"])
day_before_yesterday_close = float(day_before_yesterday["4. close"])

percentage_change = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100

if abs(percentage_change) >= 5:

    news = requests.get("https://newsapi.org/v2/everything", params=News_API_Parameters)
    news_data = news.json()

    articles = news_data.get("articles", [])
    message_articles = ""
    seen_titles = set()

    for article in articles:
        title = article.get("title")
        description = article.get("description")

        if title and description and title not in seen_titles:
            seen_titles.add(title)
            message_articles += f"Headline: {title}\n"

    message_articles = f"TSLA: {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change):.2f}%\n" + message_articles

    chunks = [message_articles[i:i + MAX_SMS_LENGTH] for i in range(0, len(message_articles), MAX_SMS_LENGTH)]
    for chunk in chunks:
        message = client.messages.create(
            body=chunk,
            from_=TWILIO_FROM_NUMBER,
            to=TO_PHONE_NUMBER
        )
        print(message.status)
        time.sleep(2)

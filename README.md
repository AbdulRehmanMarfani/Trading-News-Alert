
---

# Trading News Alert 📈📉

A Python automation script that tracks Tesla (TSLA) stock price changes and sends breaking news headlines via SMS when the stock moves significantly (5% or more). This combines real-time financial data, current news, and SMS alerts using APIs from Alpha Vantage, NewsAPI, and Twilio.

---

## Features 🚀

* **Real-Time Stock Monitoring**: Uses Alpha Vantage to check daily TSLA stock prices.
* **Dynamic News Fetching**: Gets the latest relevant Tesla news using the NewsAPI `everything` endpoint.
* **SMS Alerts**: Sends alerts directly to your phone using Twilio when a large stock movement is detected.
* **Secure Credential Management**: All sensitive data like API keys and phone numbers are handled via `.env` environment variables.

---

## How It Works ⚙️

1. Checks the last two days' closing prices for TSLA using Alpha Vantage.
2. Calculates the percentage change between them.
3. If the change is ≥5% (positive or negative):

   * Pulls 3 recent news headlines about Tesla.
   * Sends them to your phone via SMS, split into chunks if necessary.

---

## Technologies Used 🧰

* **Python**
* **Alpha Vantage API** for stock price data
* **NewsAPI** for headlines
* **Twilio** for sending SMS
* **dotenv** for handling secrets securely

---

## Setup Guide 🛠️

### 1. Clone the Repository

```bash
git clone https://github.com/AbdulRehmanMarfani/Trading-News-Alert.git
cd tesla-stock-alert
```

### 2. Install Dependencies

```bash
pip install requests twilio python-dotenv
```

### 3. Set Up Environment Variables

Create a `.env` file in the same directory and add:

```env
ALPHAVANTAGE_API_KEY=your_alpha_vantage_key
NEWS_API_KEY=your_newsapi_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_FROM_NUMBER=your_twilio_phone_number
TO_PHONE_NUMBER=your_own_phone_number
```

### 4. Run the Script

```bash
python main.py
```

> You'll receive SMS alerts if TSLA moved more than 5% since the previous trading day.

---

## Example Output 📬

If Tesla stock drops 6.4%, you might get:

```
TSLA: 🔻6.40%
Headline: Tesla shares tumble after earnings report misses Wall Street expectations
Headline: Elon Musk says Tesla is facing production challenges
Headline: Analysts question Tesla's valuation after quarterly report
```

---

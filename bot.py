import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("stock_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello! I can provide stock suggestions, analysis, top movers, predictions, and more. Use /help to see all commands.")

@app.on_message(filters.command("help"))
def help(client, message):
    help_text = """
    Available commands:
    /suggest [stock] - Get stock suggestion
    /analysis [stock] - Detailed analysis and recommendation
    /movers - Get top movers
    /export [stock] - Export stock data to Excel
    /predict [stock] - Predict stock price trend with chart
    """
    message.reply_text(help_text)

@app.on_message(filters.command("suggest"))
def suggest(client, message):
    if len(message.command) < 2:
        message.reply_text("Please provide a stock ticker symbol.")
        return

    stock = message.command[1].upper()
    ticker = yf.Ticker(stock)
    info = ticker.info

    recommendation = info.get('recommendationKey', 'N/A')
    analysis = f"""
    Stock: {stock}
    Current Price: {info.get('currentPrice', 'N/A')}
    Recommendation: {recommendation}
    Market Cap: {info.get('marketCap', 'N/A')}
    PE Ratio: {info.get('forwardPE', 'N/A')}
    """
    message.reply_text(analysis)

@app.on_message(filters.command("analysis"))
def analysis(client, message):
    if len(message.command) < 2:
        message.reply_text("Please provide a stock ticker symbol.")
        return

    stock = message.command[1].upper()
    ticker = yf.Ticker(stock)
    info = ticker.info

    # Provide more detailed analysis
    recommendation = info.get('recommendationKey', 'N/A')
    reasons = f"""
    Stock: {stock}
    Current Price: {info.get('currentPrice', 'N/A')}
    Recommendation: {recommendation}
    Market Cap: {info.get('marketCap', 'N/A')}
    PE Ratio: {info.get('forwardPE', 'N/A')}
    Why Buy/Hold/Sell: 
    - {info.get('longBusinessSummary', 'N/A')}
    - PE Ratio analysis: A lower PE ratio could indicate the stock is undervalued or the company is experiencing difficulties, while a higher PE ratio might suggest overvaluation.
    """
    message.reply_text(reasons)

@app.on_message(filters.command("movers"))
def movers(client, message):
    # Fetch top movers from Yahoo Finance
    movers = yf.get_day_most_active()
    movers_list = "\n".join([f"{m['symbol']} - {m['name']} - {m['regularMarketChangePercent']}%" for m in movers])
    message.reply_text(f"Top Movers: \n{movers_list}")

@app.on_message(filters.command("export"))
def export(client, message):
    if len(message.command) < 2:
        message.reply_text("Please provide a stock ticker symbol.")
        return

    stock = message.command[1].upper()
    ticker = yf.Ticker(stock)
    hist = ticker.history(period="1y")
    file_path = f"{stock}_data.xlsx"
    hist.to_excel(file_path)
    message.reply_document(file_path)
    os.remove(file_path)

@app.on_message(filters.command("predict"))
def predict(client, message):
    if len(message.command) < 2:
        message.reply_text("Please provide a stock ticker symbol.")
        return

    stock = message.command[1].upper()
    ticker = yf.Ticker(stock)
    hist = ticker.history(period="1y")

    # Simple moving average prediction
    hist['SMA_20'] = hist['Close'].rolling(window=20).mean()
    hist['SMA_50'] = hist['Close'].rolling(window=50).mean()

    plt.figure(figsize=(14, 7))
    plt.plot(hist['Close'], label='Close Price')
    plt.plot(hist['SMA_20'], label='20-Day SMA')
    plt.plot(hist['SMA_50'], label='50-Day SMA')
    plt.title(f'{stock} Price Prediction')
    plt.legend()
    chart_path = f"{stock}_prediction.png"
    plt.savefig(chart_path)
    plt.close()

    message.reply_photo(chart_path)
    os.remove(chart_path)

if __name__ == "__main__":
    app.run()

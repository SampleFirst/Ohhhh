import pandas as pd
import yfinance as yf
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("stock_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("Hello! I can provide stock suggestions, analysis, and movers list. Use /help to see commands.")

@app.on_message(filters.command("help"))
def help(client, message):
    help_text = """
    Available commands:
    /suggest [stock] - Get stock suggestion
    /movers - Get top movers
    /export [stock] - Export stock data to Excel
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

    recommendation = "Buy" if info['recommendationKey'] == 'buy' else "Sell"
    analysis = f"""
    Stock: {stock}
    Current Price: {info.get('currentPrice', 'N/A')}
    Recommendation: {recommendation}
    Market Cap: {info.get('marketCap', 'N/A')}
    PE Ratio: {info.get('forwardPE', 'N/A')}
    """
    message.reply_text(analysis)

@app.on_message(filters.command("movers"))
def movers(client, message):
    # Fetch top movers (e.g., using a Yahoo Finance method or an API)
    # This is just an example, replace with actual data fetching logic
    movers = "Top Movers: \n1. STOCK1\n2. STOCK2\n3. STOCK3"
    message.reply_text(movers)

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

if __name__ == "__main__":
    app.run()

markdown
# Stock Telegram Bot

This is a Telegram bot that provides stock suggestions, analysis, and top movers list, and allows exporting stock data to an Excel sheet using the Pyrogram library and Yahoo Finance API.

## Features

- `/start`: Start the bot and get a welcome message.
- `/help`: List of available commands.
- `/suggest [stock]`: Get stock suggestion with analysis.
- `/movers`: Get top movers list.
- `/export [stock]`: Export stock data to an Excel file.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-telegram-bot.git
   cd stock-telegram-bot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your API credentials:
   ```plaintext
   API_ID=your_api_id
   API_HASH=your_api_hash
   BOT_TOKEN=your_bot_token
   ```

5. Run the bot:
   ```bash
   python bot.py
   ```

## Deployment

You can deploy this bot on Render, Heroku, or any other cloud platform. Make sure to set the environment variables (`API_ID`, `API_HASH`, `BOT_TOKEN`) on the platform as well.

## License

This project is licensed under the MIT License.
```

### Step 6: Push to GitHub

1. **Initialize a new Git repository:**
   ```bash
   git init
   ```

2. **Add your files and commit:**
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

3. **Create a new repository on GitHub and add it as a remote:**
   ```bash
   git remote add origin https://github.com/your-username/stock-telegram-bot.git
   ```

4. **Push your code to GitHub:**
   ```bash
   git push -u origin master
   ```

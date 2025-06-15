# 🧮 Telegram Age Calculator Bot

A simple and fun Telegram bot that calculates your exact age from your date of birth — in years, months, days, hours, minutes, and even seconds!

## 🚀 Features

- Calculates age in:
  - ✅ Years, months, and days
  - ✅ Hours, minutes, and seconds
- Clean and friendly response format
- Built with Python and `python-telegram-bot`
- Simple to use — just send your DOB in `DD-MM-YYYY` format

## 📌 How It Works

1. Start the bot with the `/start` command.
2. Send your date of birth (e.g., `01-01-2000`).
3. Get your detailed age instantly!

Example:
```
You: 01-01-2000  
Bot: Your exact age is:  
🗓 24 years, 5 months, 14 days  
🕒 214,560 hours  
🕑 12,873,600 minutes  
⏱ 772,416,000 seconds
```

## 🛠 Tech Stack

- Python 3
- python-telegram-bot
- dateutil (for relativedelta)
- nest_asyncio

## 📦 Setup & Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/age-calculator-bot.git
cd age-calculator-bot
```

2. Install dependencies:
```bash
pip install python-telegram-bot python-dateutil nest_asyncio
```

3. Replace `"YOUR BOT KEY"` in `agecalc.py` with your actual Bot Token from [@BotFather](https://t.me/BotFather)

4. Run the bot:
```bash
python agecalc.py
```

## 🤝 Contribute

Feel free to fork the repo and suggest features or improvements via pull requests or issues.

## 📄 License

MIT License

## 👨‍💻 Author

Made with ❤️ by saicharan_sada  
🔗 [LinkedIn](https://www.linkedin.com/in/saicharan-sada/)  
💻 [GitHub](https://github.com/yourusername)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Replace this with your actual bot token
BOT_TOKEN = "YOUR BOT KEY"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! Send me your date of birth in DD-MM-YYYY format and I will calculate your exact age."
    )

# Main handler for age calculation
async def calculate_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dob_str = update.message.text.strip()
    try:
        dob = datetime.strptime(dob_str, "%d-%m-%Y")
        now = datetime.now()

        if dob > now:
            await update.message.reply_text("❌ Date of birth cannot be in the future!")
            return

        delta = relativedelta(now, dob)
        total_seconds = int((now - dob).total_seconds())
        hours = total_seconds // 3600
        minutes = total_seconds // 60
        seconds = total_seconds

        await update.message.reply_text(
            f"📊 Your exact age is:\n"
            f"🗓 {delta.years} years, {delta.months} months, {delta.days} days\n"
            f"🕒 {hours:,} hours\n"
            f"🕑 {minutes:,} minutes\n"
            f"⏱ {seconds:,} seconds"
        )
    except ValueError:
        await update.message.reply_text("❌ Please send DOB in DD-MM-YYYY format (e.g., 01-01-2000).")

# Run the bot
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate_age))

    print("🤖 Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    import nest_asyncio

    nest_asyncio.apply()
    asyncio.get_event_loop().run_until_complete(main())


import os
import logging
import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# لاگ‌ها برای دیباگ
logging.basicConfig(level=logging.INFO)

# توکن‌ها (مستقیم وارد شده؛ برای امنیت بهتر از env استفاده کن)
TELEGRAM_TOKEN = "7156009984:AAFqU7EIjCE47ZYYETn1VXcrwNCVZQdHZsM"
OPENAI_API_KEY = "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"

# تنظیم کلید OpenAI
openai.api_key = OPENAI_API_KEY

# استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من دستیار هوشمند تو هستم. هر چی خواستی بپرس یا بگو تا انجامش بدم.")

# دریافت پیام و پاسخ با ChatGPT
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}]
        )
        response = completion.choices[0].message.content.strip()
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"مشکلی پیش اومد: {e}")

# اجرای برنامه
async def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# تنظیمات لاگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور برای شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سلام! من ربات شما هستم.')

# دستور برای کمک
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('برای کمک، لطفا دستور را وارد کنید.')

# دستور برای اطلاعات
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('این ربات برای انجام کارهای مختلف طراحی شده است.')

# اصلی
async def main():
    # توکن ربات
    app = Application.builder().token("7156009984:AAFqU7EIjCE47ZYYETn1VXcrwNCVZQdHZsM").build()

    # اضافه کردن دستورات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info))

    # شروع دریافت پیام‌ها
    await app.run_polling()

# اجرای برنامه بدون استفاده از asyncio.run()
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

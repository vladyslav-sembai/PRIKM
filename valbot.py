import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Встановлюємо логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функція для отримання курсу валюти
def get_exchange_rate(currency: str) -> str:
    url = f'https://api.frankfurter.app/latest?from=USD&to={currency}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and 'rates' in data:
        rates = data['rates']
        if currency in rates:
            rate = rates[currency]
            return f'Курс {currency} до USD: {rate}'
        else:
            return 'Не вдалося знайти курс для зазначеної валюти.'
    else:
        return 'Помилка при отриманні даних з API.'

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привіт! Я бот для отримання курсів валют. Просто введіть код валюти, щоб отримати її курс до USD.')

# Обробка повідомлень з кодом валюти
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    currency = update.message.text.upper()
    rate_message = get_exchange_rate(currency)
    await update.message.reply_text(rate_message)

def main() -> None:
    # Ваш токен від BotFather
    TOKEN = '7386749945:AAHNFDac3Ue-DFI_3U6fW5-jEvRFPU58HIk'

    # Створюємо ApplicationBuilder та реєструємо команди
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаємо бота
    application.run_polling()

if __name__ == '__main__':
    main()

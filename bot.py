"""
This is a echo bot.
It echoes any incoming text messages.
"""
import wikipedia
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'bot tokeningizni yozing'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

wikipedia.set_lang("uz")
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hey wikipedia botiga xush kelibsiz")



@dp.message_handler()
async def send_wiki(message: types.Message):
    try:
        response = wikipedia.summary(message.text)
    except:
        response = "Bunday maqola topilmadi"
    await message.answer(response)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

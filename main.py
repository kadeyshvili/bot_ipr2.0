from telebot.async_telebot import AsyncTeleBot

TOKEN = '5816165685:AAEwUonRjzVpdYdv26rfjy37L2hw1UC1bBY'
bot = AsyncTeleBot(TOKEN)

from handlers import *
from modules import GameManager

manager = GameManager()

if __name__ == '__main__':
    asyncio.run(bot.polling(non_stop=True))
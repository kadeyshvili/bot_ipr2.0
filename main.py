from telebot.async_telebot import AsyncTeleBot

TOKEN = ''
bot = AsyncTeleBot(TOKEN)

from handlers import *
from modules import GameManager

manager = GameManager()

if __name__ == '__main__':
    asyncio.run(bot.polling(non_stop=True))

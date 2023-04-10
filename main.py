import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

# PROXY_URL = 'http://proxy.server:3128'
bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends '/start' or '/help' command
    :param message:
    :return:
    """
    await message.reply('Hi!\nIm echobot!\nPowered by aiogram.')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
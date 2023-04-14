import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

# PROXY_URL = 'http://proxy.server:3128'
# bot = Bot(token=os.environ.get('TOKEN'), proxy=PROXY_URL)
bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends '/start' or '/help' command
    :param message:
    :return:
    """
    await message.reply(
        'Привет!\n\nЯ создаю сайты и продвигаю их в сети интернет!\nЕсли сайт уже есть, могу предложить сео-оптимизацию!\n\nЧтобы узнать больше наберите /help')


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends '/help' command
    :param message:
    :return:
    """
    await message.reply('Команды, которые я понимаю:\n\nзаказать сайт - /site\nзаказать сео-оптимизацию - /seo')


@dp.message_handler(commands=['site'])
async def send_site(message: types.Message):
    """
    This handler will be called when user sends '/site' command
    :param message:
    :return:
    """
    await message.reply('Чтобы создать для Вас новый сайт, я зову своего создателя)\n\nХорошего дня!')


@dp.message_handler(commands=['seo'])
async def send_site(message: types.Message):
    """
    This handler will be called when user sends '/seo' command
    :param message:
    :return:
    """
    await message.reply('Чтобы продвинуть Ваш сайт, мне нужно позвать своего создателя)\n\nХорошего дня!')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

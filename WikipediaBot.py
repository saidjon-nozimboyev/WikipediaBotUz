import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6437218316:AAE71U1aIc9E677laxoSUEEyIItRfb2AaAk'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang("uz")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nThis bot finds information in Uzbek language.")

@dp.message_handler()
async def WikiInfo(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bunday ma'lumot topilmadi!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

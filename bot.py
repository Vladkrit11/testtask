import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram.filters import Command
import asyncio
import sys
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN = '7296874938:AAEzEWDcMlI4sOT7dfXDe3ubwWnmEAakAsk'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def send_welcome(message: Message):
    await message.reply("Привіт! Використай команду /get_today_statistic щоб отримати статистику за останню годину.")

@dp.message(Command('get_today_statistic'))
async def send_statistic(message: Message):
    try:       
        document = FSInputFile('vacancies.xlsx')
        await bot.send_document(message.chat.id, document)
    except Exception as e:
        logging.error(f"Помилка при відправці файлу: {e}")
        await message.reply("Виникла помилка при відправці статистики.")
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    
    await dp.start_polling(bot)
    
if __name__ == '__main__':
     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
     asyncio.run(main())

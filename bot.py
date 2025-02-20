import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandObject
# import requests
import asyncio
from userbot.config import BOT_TOKEN
import gift_handler


async def main():

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(gift_handler.router)


    

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
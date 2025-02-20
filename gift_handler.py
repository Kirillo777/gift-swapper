from aiogram import Bot, Dispatcher, types
from aiogram import Router, F, types
from aiogram.filters import Command, CommandObject
from userbot.config import BOT_TOKEN
# import requests

router = Router()

bot = Bot(token=BOT_TOKEN)

@router.message(Command("list_gifts"))
async def handle_messages(message: types.Message):


    # Здесь логика для обработки улучшения подарка
    # Получаем список доступных подарков
    gifts = await bot.get_available_gifts()
    # sticker_file_ids = [gift[1]['file_id'] for gift in gifts]
    
    # Проверяем, есть ли подарки
    # if gifts:

        # for gift in gifts.gifts:
        # Формируем строку с информацией о каждом подарке
            # gift_list = '\n'.join([f"{gift.sticker.file_id}" for gift in gifts.gifts])


    # for sticker_id in sticker_file_ids:

    #     await message.answer_sticker(sticker_id)

    for gift in gifts:
        sticker_id = gift.is_video
        await message.answer(sticker_id)
    
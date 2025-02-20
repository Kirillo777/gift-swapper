from pyrogram import Client
from config import api_hash, api_id
import asyncio

api_id = api_id
api_hash = api_hash

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")
        user = "@looo1112"
        async for gift in app.get_chat_gifts(user):
            await app.send_message("me", gift)


asyncio.run(main())
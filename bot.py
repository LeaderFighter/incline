# SCRIPT MADE BY @H1M4N5HU0P


import asyncio
import os
import time
import logging
from decouple import config
from telethon.sync import TelegramClient
from telethon.sessions import StringSession


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


STRING_SESSION = config("STRING_SESSION", default=None)

COUNT = config("COUNT", default=None)

CHATID = config("CHATID", default=None)

MESSAGE = config("MESSAGE", default=None)

API_ID = 2184829 

API_HASH = "6930b92388baabff4cb4a1d377085035"

# bot_token = input("Enter You're Bot Token: ")


async def main():
    async with TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH) as bot:
        print("Spam Started Successfully")
        try:
            for i in range(int(COUNT)):
                try:
                    await bot.send_message(int(CHATID), MESSAGE)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

    bot.start()
asyncio.run(main())

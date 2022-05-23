import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from environment import API_ID, API_HASH, STRING_SESSION

jmthon = TelegramClient(StringSession(str(STRING_SESSION)), int(API_ID), str(API_HASH)).start()




print("- تم بنجاح تشغيل سورس جمثون المؤقت")

jmthon.run_until_disconnected()

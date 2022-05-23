import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from environment import API_ID, API_HASH, STRING_SESSION

jmthon = TelegramClient(StringSession(str(STRING_SESSION)), int(API_ID), str(API_HASH)).start()

async def join_channel():
    try:
        await jmthon(JoinChannelRequest("@jmthon"))
    except BaseException:
        pass
    try:
        await jmthon(JoinChannelRequest("@TeamJmthon"))
    except BaseException:
        pass



print("- تم بنجاح تشغيل سورس جمثون المؤقت")

jmthon.loop.create_task(join_channel())
jmthon.run_until_disconnected()

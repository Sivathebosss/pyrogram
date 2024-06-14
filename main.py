from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, ReplyKeyboardMarkup
import asyncio
import config as C






Siva = Client(
      name="pyrogram",
      api_id=C.API_ID,
      api_hash=C.API_HASH,
      bot_token=C.BOT_TOKEN
)

STATS = [[
 InlineKeyboardButton("data", callback_data="start")
]]

HI = f""" 
Hello, 
I am working perfectly"""

@Siva.on_message(filters.command("start"))
async def start_cmd(client, message):
    rep = await message.reply_text("`Hi, I am starting`") 
    await asyncio.sleep(1)
    await rep.delete()
    await message.reply_text(
        text="Hello welcome back"
    )





print("Bot started")

Siva.run()

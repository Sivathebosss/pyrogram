from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID="14486797"
API_HASH="bf3b9df595c63aab3052f43fe1939068"
BOT_TOKEN="5461167123:AAHqanDb4568Wlt2gVtoY41248j_XyQ6pkM"


Siva = Client(
      name="pyrogram",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN
)

STATS = [[
 InlineKeyboardButton("hi", url="t.me/Sivatheking_1")
]]

@Siva.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        text="Hello welcome back",
        reply_markup=InlineKeyboardMarkup(STATS)
    )







print("Bot started")

Siva.run()

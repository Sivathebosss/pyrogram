from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, ReplyKeyboardMarkup
import asyncio




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
 InlineKeyboardButton("data", callback_data="start")
]]

HI = f""" 
Hello {msg.from_user.mention}
I am working perfectly"""

@Siva.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        text="Hello welcome back",
        reply_markup=InlineKeyboardMarkup(STATS)
    )

@Siva.on_callback_query()
async def callback_query(client, msg: CallbackQuery):
    if msg.data == "start":

       reply1 = await msg.message("I am working"),
       await asyncio.sleep(0.4),
       await reply1.message("I am working")





print("Bot started")

Siva.run()

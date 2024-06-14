from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, ReplyKeyboardMarkup
import asyncio
import Config as C






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
    await message.reply_text(
        text="Hello welcome back",
        reply_markup=InlineKeyboardMarkup(STATS)
    )

@Siva.on_callback_query()
async def callback_query(client, msg: CallbackQuery):
    if msg.data == "start":

       reply1 = await msg.message.edit("I am working"),
       await asyncio.sleep(0.4),
       await reply1.edit(HI)





print("Bot started")

Siva.run()

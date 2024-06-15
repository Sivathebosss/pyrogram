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
CHARACTER: Cho Kyuhwan
Type: Mage
Rank: C

Strength: 55
Agility: 65
Stamina: 50
Intelligence: 35
Perception: 45"""

@Siva.on_message(filters.command("start"))
async def start_cmd(client, message):
    rep = await message.reply_text("`Hi, I am starting`") 
    await asyncio.sleep(1)
    await rep.delete()
    await message.reply_text(
        text="Hello welcome back"
    )
@Siva.on_message(filters.command("data")) 
async def data_cmd(client, msg):
      if msg.text == "/data":
            await msg.reply_text("Give me character name \nEx:- /data Cho Kyuhwan") 
      if msg.text == "/data Cho Kyuhwan":
            await msg.reply_text(HI) 
      else:
            await msg.reply_text(" Please provide valid character name") 
      




print("Bot started")

if __name__ == '__main__':
    Siva.run(port=8000)
     

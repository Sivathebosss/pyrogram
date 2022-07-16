from pyrogram import Client, filters

API_ID="14486797"
API_HASH="bf3b9df595c63aab3052f43fe1939068"
BOT_TOKEN="5461167123:AAHqanDb4568Wlt2gVtoY41248j_XyQ6pkM"


Siva = Client(
      name="pyrogram",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN
)

@Siva.on_message(filers.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Hello welcome back")







print("Bot started")

Siva.run()

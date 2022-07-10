from pyrogram import Client, filters

API_ID=""
API_HASH=""
BOT_TOKEN=""


Siva = Client(
      name="pyrogram",
      api_id="API_ID",
      api_hash="API_HASH",
      bot_token="BOT_TOKEN",
)
@Siva.on_command(filers.command("start"))
anyc def start_cmd(bot, message):
    await message.reply_text("Hello welcome back")







print("Bot started")

Siva.run()

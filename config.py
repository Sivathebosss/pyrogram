import os
class Config(object):
     
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")

    API_ID = os.getenv("API_ID", 12345))

    API_HASH = os.getenv("API_HASH", "")

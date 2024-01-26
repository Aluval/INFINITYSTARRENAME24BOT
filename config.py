from os import environ
import os

API_ID = int(os.environ.get("API_ID", "10811400"))
API_HASH = os.environ.get("API_HASH", "191bf5ae7a6c39771e7b13cf4ffd1279")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6487202001:AAHCk-mmxZ0wLTMUL4QYTqsXOjDuMCJQrTo")
ADMIN = int(os.environ.get("ADMIN", "6469754522"))  
SUDO_USERS = os.environ.get("SUDO_USERS", "6469754522, 6621835067")
CAPTION = os.environ.get("CAPTION", "")
DB_NAME = os.environ.get("DB_NAME","Sunrises_24")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://RAINBOWRENAME24BOT:<password>@cluster0.ud3toaz.mongodb.net/?retryWrites=true&w=majority")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002112896731"))
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))

# for thumbnail ( back end is MrMKN brain 😉)
DOWNLOAD_LOCATION = "./DOWNLOADS"


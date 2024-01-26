from os import environ
import os

API_ID = int(os.environ.get("API_ID", "10811400"))
API_HASH = os.environ.get("API_HASH", "191bf5ae7a6c39771e7b13cf4ffd1279")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6487202001:AAHCk-mmxZ0wLTMUL4QYTqsXOjDuMCJQrTo")
ADMIN = int(os.environ.get("ADMIN", "6469754522"))  
SUDO_USERS = os.environ.get("SUDO_USERS", "6469754522, 6621835067")
CAPTION = os.environ.get("CAPTION", "")
AUTH_USERS = int(os.environ.get("AUTH_USERS", "6469754522"))
HEROKU_API = os.environ.get("HEROKU_API", "7b47e8fc-fc54-4344-b15a-b3c7a119f763")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "vast-tundra-32655")


# for thumbnail ( back end is MrMKN brain 😉)
DOWNLOAD_LOCATION = "./DOWNLOADS"


import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ُꪀٰ᥆ُVꪜُᥲ ُꪔٰυٰ᥉ٰᎥٰᥴ")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "IIIT2")
ALIVE_NAME = getenv("ALIVE_NAME", "OLiver")
BOT_USERNAME = getenv("BOT_USERNAME", "RLRLbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GPVVV")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "NNNB9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZZZZ7LZ")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ".").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Oliver-zr/z")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/4763d6135a6dec50390b7.jpg")

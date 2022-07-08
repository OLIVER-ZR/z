import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBoxqqMj0Fksa5hPTLpZ_oBW7cUS0BR6L4G1GveRPZTmIaW4Pe2hdBVdN-OsoOa16FUdUk1hVMhDDsJ7icUKU3w3rNy19-gWX6vB82zndYvIUpm5XNaJNs3bGdVnlSn-GGmbaXJAQ5K6y852A9Lb8HHtWuwuqSGvd1zgFfwglkowNqylmFibtZkZ83GKNxJS_nH_uE5fGYucwHdA_HMjviUxozYWKrOxoXWXj4uukoyDn4uYmH5bi_tyGRUBUvcya8IeGnO7z2NyHnezxs4yj_fCPiKLZz40O1kDdSutMOPuekS59bcVSYZdUfSVxU11Z7_jOWZf_QSS0NlCq9UKjjhAAAAATnzUQsA")
BOT_TOKEN = getenv("BOT_TOKEN", "5578917997:AAHzh1hdiiKWC69t-8R0l_9lP_IKNBtEbsE")
BOT_NAME = getenv("BOT_NAME", "ُꪀٰ᥆ُVꪜُᥲ ُꪔٰυٰ᥉ٰᎥٰᥴ")
API_ID = int(getenv("API_ID", "16455004"))
API_HASH = getenv("API_HASH", "7fbdee2476a83b78f8fdee9ba9f41cdf")
OWNER_NAME = getenv("OWNER_NAME", "IIIT2")
ALIVE_NAME = getenv("ALIVE_NAME", "OLiver")
BOT_USERNAME = getenv("BOT_USERNAME", "RLRLbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GPVVV")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "NNNB9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZZZZ7LZ")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5036835528").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c354364952713db1a3360.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Oliver-zr/z")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c354364952713db1a3360.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/c354364952713db1a3360.jpg")

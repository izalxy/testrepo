import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7877809099").split()))

API_ID = int(os.getenv("API_ID", "34133587"))

API_HASH = os.getenv("API_HASH", "faeffa47a5a9877566e2ab18d6d19355")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8312358716:AAFzzgFPvQSLukwqmNLOeJyqW8qVywcSjrM")

OWNER_ID = int(os.getenv("OWNER_ID", "7877809099"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1003192483568").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://anjyya8_db_user:anjy123@cluster0.pfj1xuc.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003457368110"))

from motor.motor_asyncio import AsyncIOMotorClient

from zall.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.userbotxx

from zall.core.database.expired import *
from zall.core.database.userbot import *
from zall.core.database.two_factor import *
from zall.core.database.pref import *
from zall.core.database.variabel import *
from zall.core.database.antigcast import *
# arthmonitor/db/db_manager.py

from tortoise import Tortoise
from db_config import TORTOISE_ORM

_initialized = False

async def init():
    global _initialized
    if not _initialized:
        await Tortoise.init(config=TORTOISE_ORM)
        await Tortoise.generate_schemas()
        _initialized = True

async def shutdown():
    if _initialized:
        await Tortoise.close_connections()

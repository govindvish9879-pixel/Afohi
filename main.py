from config import Config
from database.naruto import *
from pyrogram import Client, idle
import asyncio, logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(sinha)
LOGGER.info("Live log streaming to telegram.")
plugins = dict(root="plugins")
if __name__ == "__main__":
    bot = Client(
        "Master",
        bot_token=Config.8160173494:AAEC4vBsfo5z89sGYRLD-M2a6-gEfSlQ8U8,
        api_id=Config.33383151,
        api_hash=Config.a1b51f828a72a0b89df9c0db86a601e1,
        sleep_threshold=120,
        plugins=plugins,
        workers=10000,
    )
    async def main():
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started --->")
        await idle()
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info("<--- Bot Stopped --->")

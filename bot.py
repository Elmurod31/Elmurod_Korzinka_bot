import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from commands import router as commands_router
from handlears import router as handlears_router
from aiogram.client.session.aiohttp import AiohttpSession
session = AiohttpSession(proxy="http://proxy.server:3128")
load_dotenv()

TOKEN = getenv("TOKEN")
bot = Bot(token=TOKEN, session=session)
# bot = Bot(token=TOKEN)
dp = Dispatcher()


dp.include_router(commands_router)
dp.include_router(handlears_router)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())
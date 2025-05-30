import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from commands import router as commands_router
from handlears import router as handlears_router

load_dotenv()

TOKEN = getenv("TOKEN")

dp = Dispatcher()


dp.include_router(commands_router)
dp.include_router(handlears_router)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())
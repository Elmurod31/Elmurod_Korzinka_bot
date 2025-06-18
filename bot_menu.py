from aiogram.types import BotCommand, Message


async def set_bot_menu(bot):
    command = [
        BotCommand(command="start", description="Botni boshlash!"),
        BotCommand(command="help", description="Yordam!")
    ]
    await bot.set_my_commands(commands=command)
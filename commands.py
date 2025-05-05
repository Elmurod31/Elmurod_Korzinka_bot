from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboard import korzinka_btn

router = Router()


@router.message(F.text == "/start")
async def command_start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Korzinka botiga xush kelibsiz 👋\nDavom etish uchun tilni tanlang ⬇️",
        reply_markup=korzinka_btn
    )
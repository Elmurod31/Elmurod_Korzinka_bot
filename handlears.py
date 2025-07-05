import os

from aiogram import F, Router, types
from aiogram.types import Message, FSInputFile

from keyboard import korzinka_btn2, korzinka_btn2_ru, korzinka_btn2_en, korzinka_btn
from lang_texts import t
from state import user_langs

router = Router()






@router.callback_query(lambda c: c.data in ['lang_uz', 'lang_ru', 'lang_en'])
async def til_bosilganda(callback_query: types.CallbackQuery):
    lang_code = callback_query.data.split("_")[1]
    user_id = callback_query.from_user.id
    user_langs[user_id] = lang_code  # Tilni saqlaymiz

    # ReplyKeyboard tanlash
    if lang_code == "ru":
        reply_kb = korzinka_btn2_ru
    elif lang_code == "en":
        reply_kb = korzinka_btn2_en
    else:
        reply_kb = korzinka_btn2

    await callback_query.message.answer("Til tanlandi ✅", reply_markup=reply_kb)
    await callback_query.answer()

    @router.message(F.text.in_([
        "O'zbek tili 🇺🇿",
        "Rus tili 🇷🇺",
        "English 🇬🇧"
    ]))
    async def change_language_reply(message: Message):
        user_id = message.from_user.id

        if message.text == "Rus tili 🇷🇺":
            lang_code = "ru"
            reply_kb = korzinka_btn2_ru
        elif message.text == "English 🇬🇧":
            lang_code = "en"
            reply_kb = korzinka_btn2_en
        else:
            lang_code = "uz"
            reply_kb = korzinka_btn2

        user_langs[user_id] = lang_code
        await message.answer("Til tanlandi ✅", reply_markup=reply_kb)


@router.message(F.text.in_([
    "Korzinka kartasi 💳", "Карта Korzinka 💳", "Korzinka Card 💳"
]))
async def command_card_handler(message: Message):
    lang = user_langs.get(message.from_user.id, "uz")
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_1.png")
    if lang =="ru":
        img_path = img_path = os.path.join(os.path.dirname(__file__), "images", "img_8.png")
    elif lang =="en":
        img_path = img_path = os.path.join(os.path.dirname(__file__), "images", "img_9.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption=t("card_caption", lang))



@router.message(F.text.in_([
    "⚡️ “Yanada arzon narx” dasturi", "⚡️ Программа «Ещё дешевле»", "⚡️ “Even Lower Price” Program"
]))
async def command_end_handler(message: Message):
    lang = user_langs.get(message.from_user.id, "uz")
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_4.png")
    if lang =="ru":
        img_path = img_path = os.path.join(os.path.dirname(__file__), "images", "img_10.png")
    elif lang =="en":
        img_path = img_path = os.path.join(os.path.dirname(__file__), "images", "img_11.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption=t("cheap_program_caption", lang))


@router.message(F.text.in_([
    "Chegirma va aktsiyalar 🔥", "Скидки и акции 🔥", "Discounts and Promotions 🔥"
]))
async def command_end_handler(message: Message):
    lang = user_langs.get(message.from_user.id, "uz")
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_5.png")
    if lang =="ru":
        img_path = img_path = os.path.join(os.path.dirname(__file__), "images", "img_12.png")
    elif lang =="en":
        img_path = img_path = os.path.join(os.path.dirname(__file__), "images", "img_13.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption=t("discounts_caption", lang))



@router.message(F.text.in_([
    "Harid qilish uchun so'vg'alar 🔱", "Подарки за покупки 🔱", "Gifts for Shopping 🔱"
]))
async def command_end_handler(message: Message):
    lang = user_langs.get(message.from_user.id, "uz")
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_6.png")
    if lang =="ru":
        img_path = img_path = os.path.join(os.path.dirname(__file__), "images", "img_14.png")
    elif lang =="en":
        img_path = img_path = os.path.join(os.path.dirname(__file__), "images", "img_15.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption=t("gifts_caption", lang))


@router.message(F.text.in_([
    "Filiallar 🏘", "Филиалы 🏘", "Branches 🏘",
]))

async def command_end_handler(message: Message):
    lang = user_langs.get(message.from_user.id, "uz")
    img_path = os.path.join(os.path.dirname(__file__), "images", "img_7.png")
    img = FSInputFile(img_path)
    await message.answer_photo(photo=img, caption=t("see_location_btn", lang))

    latitude = 41.319593583706656
    longitude = 69.27619793880801
    await message.answer_location(latitude, longitude)

@router.message(F.text == "🔁 Tilni o‘zgartirish")
async def tilni_ozgartirish(message: Message):
    await message.answer("Tilni tanlang:", reply_markup=korzinka_btn)


@router.message(F.text == "🔁 Изменить язык")
async def tilni_ozgartirish(message: Message):
    await message.answer("Tilni tanlang:", reply_markup=korzinka_btn)

@router.message(F.text == "🔁 Select language")
async def tilni_ozgartirish(message: Message):
    await message.answer("Tilni tanlang:", reply_markup=korzinka_btn)
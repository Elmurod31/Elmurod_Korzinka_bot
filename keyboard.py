from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

korzinka_btn = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="O'zbek tili 🇺🇿", callback_data="lang_uz")],
            [InlineKeyboardButton(text="Rus tili 🇷🇺", callback_data="lang_ru")],
            [InlineKeyboardButton(text="Ingliz 🇬🇧", callback_data="lang_en")]
],resize_keyboard=True)

korzinka_btn2 = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="Korzinka kartasi 💳"), KeyboardButton(text="⚡️ “Yanada arzon narx” dasturi"),],
    [KeyboardButton(text="Chegirma va aktsiyalar 🔥"), KeyboardButton(text="Harid qilish uchun so'vg'alar 🔱")],
    [KeyboardButton(text="Filiallar 🏘")]
],resize_keyboard=True)



korzinka_btn2_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Карта Korzinka 💳"), KeyboardButton(text="⚡️ Программа «Ещё дешевле»")],
        [KeyboardButton(text="Скидки и акции 🔥"), KeyboardButton(text="Подарки за покупки 🔱")],
        [KeyboardButton(text="Филиалы 🏘")]
    ],
    resize_keyboard=True
)

korzinka_btn2_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Korzinka Card 💳"), KeyboardButton(text="⚡️ “Even Lower Price” Program")],
        [KeyboardButton(text="Discounts and Promotions 🔥"), KeyboardButton(text="Gifts for Shopping 🔱")],
        [KeyboardButton(text="Branches 🏘")]
    ],
    resize_keyboard=True
)
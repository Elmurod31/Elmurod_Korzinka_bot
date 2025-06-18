from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

web_app = WebAppInfo(url="https://elmurod31.github.io/Elmurod_Korzinka_bot/")
korzinka_btn = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="O'zbek tili 🇺🇿", callback_data="lang_uz")],
            [InlineKeyboardButton(text="Rus tili 🇷🇺", callback_data="lang_ru")],
            [InlineKeyboardButton(text="Ingliz 🇬🇧", callback_data="lang_en")]
],resize_keyboard=True)

korzinka_btn2 = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text="Korzinka kartasi 💳"), KeyboardButton(text="⚡️ “Yanada arzon narx” dasturi"),],
    [KeyboardButton(text="Chegirma va aktsiyalar 🔥"), KeyboardButton(text="Harid qilish uchun so'vg'alar 🔱")],
    [KeyboardButton(text="Menu", web_app=web_app), KeyboardButton(text="Filiallar 🏘")],
    [KeyboardButton(text="🔁 Tilni o‘zgartirish")]
],resize_keyboard=True)



korzinka_btn2_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Карта Korzinka 💳"), KeyboardButton(text="⚡️ Программа «Ещё дешевле»")],
        [KeyboardButton(text="Скидки и акции 🔥"), KeyboardButton(text="Подарки за покупки 🔱")],
        [KeyboardButton(text="Меню", web_app=web_app), KeyboardButton(text="Филиалы 🏘")],
        [KeyboardButton(text="🔁 Изменить язык")]
    ],
    resize_keyboard=True
)

korzinka_btn2_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Korzinka Card 💳"), KeyboardButton(text="⚡️ “Even Lower Price” Program")],
        [KeyboardButton(text="Discounts and Promotions 🔥"), KeyboardButton(text="Gifts for Shopping 🔱")],
        [KeyboardButton(text="Menu", web_app=web_app), KeyboardButton(text="Branches 🏘")],
        [KeyboardButton(text="🔁 Select language")]
    ],
    resize_keyboard=True
)
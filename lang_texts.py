# lang_texts.py

texts = {
    "uz": {
        "card_caption": "Xaridlaringiz uchun Korzinka kartangizga keshbek oling, balansingizni kuzatib boring va aksiyalardan xabardor bo‘ling 💌",
        "card_btn": "Korzinka kartasi 💳",
        "cheap_program_btn": "⚡️ “Yanada arzon narx” dasturi",
        "cheap_program_caption": "⚡️ Sizga mehr bilan biz kundalik xaridlar tovarlariga yanada arzon narxlar dasturi — Yanada arzon narxni boshladik!\n\n📣 Ushbu tovarlar bilan saytimizdagi Yanada arzon narx katalogida tanishishingiz mumkin.",
        "discounts_btn": "Chegirma va aktsiyalar 🔥",
        "discounts_caption": "📌 Supermarketlarimizda har doim tovarlarga chegirmalar va ajoyib chegirmalar mavjud.",
        "gifts_btn": "Harid qilish uchun so'vg'alar 🔱",
        "gifts_caption": "Aksiyalarda qatnashing va supersovrinlar yuting! 🥳",
        "see_location_btn": "Filiallar 🏘",
        "menu_btn": "Menyu",
    },
    "ru": {
        "card_caption": "Получайте кэшбэк на карту Korzinka за покупки, следите за балансом и узнавайте об акциях 💌",
        "card_btn": "Карта Korzinka 💳",
        "cheap_program_btn": "⚡️ Программа «Ещё дешевле»",
        "cheap_program_caption": "⚡️ С любовью мы начали программу «Ещё дешевле» на повседневные товары!\n\n📣 Ознакомьтесь с каталогом на сайте.",
        "discounts_btn": "Скидки и акции 🔥",
        "discounts_caption": "📌 В наших супермаркетах всегда есть скидки и акции на товары.",
        "gifts_btn": "Подарки за покупки 🔱",
        "gifts_caption": "Участвуйте в акциях и выигрывайте суперпризы! 🥳",
        "see_location_btn": "Филиалы 🏘",
        "menu_btn": "Меню",
    },
    "en": {
        "card_caption": "Get cashback on your Korzinka card, track your balance, and stay informed about promotions 💌",
        "card_btn": "Korzinka Card 💳",
        "cheap_program_btn": "⚡️ “Even Lower Price” Program",
        "cheap_program_caption": "⚡️ With love, we launched the 'Even Lower Price' program for daily shopping!\n\n📣 Check out the catalog on our website.",
        "discounts_btn": "Discounts and Promotions 🔥",
        "discounts_caption": "📌 Our supermarkets always have discounts and great deals.",
        "gifts_btn": "Gifts for Shopping 🔱",
        "gifts_caption": "Participate in promotions and win super prizes! 🥳",
        "see_location_btn": "Branches 🏘",
        "menu_btn": "Menu",
    }
}


def t(key: str, lang: str = "uz"):
    return texts.get(lang, texts["uz"]).get(key, key)

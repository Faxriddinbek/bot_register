from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language = InlineKeyboardMarkup( # umumioy yuiboriladigon buttonlarini jamlammasi
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Python", callback_data="py"),#callback_data => shu tugmani bosganda orqa fonda ishlaydigon text bu userga ko'rinmidi
            InlineKeyboardButton(text="JavaScript", callback_data="js")
        ],
        [
            InlineKeyboardButton(text="PHP", callback_data="php"),
            InlineKeyboardButton(text="GO", callback_data="go")
        ]
    ]
)
inline_keyboard_test = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Test", callback_data="inline_keyboard")
        ]
    ]
)
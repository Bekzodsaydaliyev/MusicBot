from aiogram.types import *

InMp3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿Uzb', callback_data="uzb"),
            InlineKeyboardButton(text='🇷🇺Rus', callback_data="rus"),
            InlineKeyboardButton(text='🇺🇲Zarubej', callback_data="zarubej")
        ],
        [
            InlineKeyboardButton(text="⬅Back", callback_data="back_start")
        ]
    ],
)

InArtist = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ummon", callback_data="ummon"),
            InlineKeyboardButton(text="Benom", callback_data="benom")
        ],
        [
            InlineKeyboardButton(text="Yulduz Usmonova", callback_data="yulduz_usmonova")
        ],
        [
            InlineKeyboardButton(text="Mband", callback_data="mband"),
            InlineKeyboardButton(text="Jony", callback_data="jony")
        ],
        [
            InlineKeyboardButton(text="Blackstar", callback_data='blackstar')
        ],
        [
            InlineKeyboardButton(text="Tentaction", callback_data="tentaction"),
            InlineKeyboardButton(text="Billie Eilish", callback_data="billie_eilish")
        ],
        [
            InlineKeyboardButton(text="Michel Jakson", callback_data="michel_jakson")
        ]
    ],
)

InLike = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👍", callback_data="like"),
            InlineKeyboardButton(text="❌", callback_data="otmen"),
            InlineKeyboardButton(text="👎", callback_data="dis_like")
        ]
    ],
)

InMichel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1michel"),
            InlineKeyboardButton(text="2", callback_data="2michel"),
            InlineKeyboardButton(text="3", callback_data="3michel"),
            InlineKeyboardButton(text="4", callback_data="4michel"),
            InlineKeyboardButton(text="5", callback_data="5michel")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6michel"),
            InlineKeyboardButton(text="7", callback_data="7michel"),
            InlineKeyboardButton(text="8", callback_data="8michel"),
            InlineKeyboardButton(text="9", callback_data="9michel"),
            InlineKeyboardButton(text="10", callback_data="10michel")
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="tentactionga"),
            InlineKeyboardButton(text="❌", callback_data="ochirish")
        ]
    ],
)

InUmmon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1ummon"),
            InlineKeyboardButton(text="2", callback_data="2ummon"),
            InlineKeyboardButton(text="3", callback_data="3ummon"),
            InlineKeyboardButton(text="4", callback_data="4ummon"),
            InlineKeyboardButton(text="5", callback_data="5ummon")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6ummon"),
            InlineKeyboardButton(text="7", callback_data="7ummon"),
            InlineKeyboardButton(text="8", callback_data="8ummon"),
            InlineKeyboardButton(text="9", callback_data="9ummon"),
            InlineKeyboardButton(text="10", callback_data="10ummon")
        ],
        [
            InlineKeyboardButton(text="❌", callback_data="ochirish"),
            InlineKeyboardButton(text="⏩", callback_data="yulduzga")
        ]
    ],
)

InYulduz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1yulduz"),
            InlineKeyboardButton(text="2", callback_data="2yulduz"),
            InlineKeyboardButton(text="3", callback_data="3yulduz"),
            InlineKeyboardButton(text="4", callback_data="4yulduz"),
            InlineKeyboardButton(text="5", callback_data="5yulduz")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6yulduz"),
            InlineKeyboardButton(text="7", callback_data="7yulduz"),
            InlineKeyboardButton(text="8", callback_data="8yulduz"),
            InlineKeyboardButton(text="9", callback_data="9yulduz"),
            InlineKeyboardButton(text="10", callback_data="10yulduz")
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="uzb"),
            InlineKeyboardButton(text="❌", callback_data="ochirish"),
            InlineKeyboardButton(text="⏩", callback_data="benomga")
        ]
    ],
)

InBlackstart = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1black"),
            InlineKeyboardButton(text="2", callback_data="2black"),
            InlineKeyboardButton(text="3", callback_data="3black"),
            InlineKeyboardButton(text="4", callback_data="4black"),
            InlineKeyboardButton(text="5", callback_data="5black")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6black"),
            InlineKeyboardButton(text="7", callback_data="7black"),
            InlineKeyboardButton(text="8", callback_data="8black"),
            InlineKeyboardButton(text="9", callback_data="9black"),
            InlineKeyboardButton(text="10", callback_data="10black"),
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="jonyga"),
            InlineKeyboardButton(text="❌", callback_data="ochirish")
        ]
    ],
)

InTentaction = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1tentaction"),
            InlineKeyboardButton(text="2", callback_data="2tentaction"),
            InlineKeyboardButton(text="3", callback_data="3tentaction"),
            InlineKeyboardButton(text="4", callback_data="4tentaction"),
            InlineKeyboardButton(text="5", callback_data="5tentaction")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6tentaction"),
            InlineKeyboardButton(text="7", callback_data="7tentaction"),
            InlineKeyboardButton(text="8", callback_data="8tentaction"),
            InlineKeyboardButton(text="9", callback_data="9tentaction"),
            InlineKeyboardButton(text="10", callback_data="10tentaction")
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="rus"),
            InlineKeyboardButton(text="❌", callback_data="ochirish"),
            InlineKeyboardButton(text="⏩", callback_data="michelga")
        ]
    ],
)

InBenom = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1benom"),
            InlineKeyboardButton(text="2", callback_data="2benom"),
            InlineKeyboardButton(text="3", callback_data="3benom"),
            InlineKeyboardButton(text="4", callback_data="4benom"),
            InlineKeyboardButton(text="5", callback_data="5benom")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6benom"),
            InlineKeyboardButton(text="7", callback_data="7benom"),
            InlineKeyboardButton(text="8", callback_data="8benom"),
            InlineKeyboardButton(text="9", callback_data="9benom"),
            InlineKeyboardButton(text="10", callback_data="10benom")
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="yulduzga"),
            InlineKeyboardButton(text="❌", callback_data="ochirish")
        ]
    ],
)

InJony = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1jony"),
            InlineKeyboardButton(text="2", callback_data="2jony"),
            InlineKeyboardButton(text="3", callback_data="3jony"),
            InlineKeyboardButton(text="4", callback_data="4jony"),
            InlineKeyboardButton(text="5", callback_data="5jony")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6jony"),
            InlineKeyboardButton(text="7", callback_data="7jony"),
            InlineKeyboardButton(text="8", callback_data="8jony"),
            InlineKeyboardButton(text="9", callback_data="9jony"),
            InlineKeyboardButton(text="10", callback_data="10jony")
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="mbandga"),
            InlineKeyboardButton(text="❌", callback_data="ochirish"),
            InlineKeyboardButton(text="⏩", callback_data="blackstarga")
        ]
    ],
)

InMband = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1mband"),
            InlineKeyboardButton(text="2", callback_data="2mband"),
            InlineKeyboardButton(text="3", callback_data="3mband"),
            InlineKeyboardButton(text="4", callback_data="4mband"),
            InlineKeyboardButton(text="5", callback_data="5mband")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6mband"),
            InlineKeyboardButton(text="7", callback_data="7mband"),
            InlineKeyboardButton(text="8", callback_data="8mband"),
            InlineKeyboardButton(text="9", callback_data="9mband"),
            InlineKeyboardButton(text="10", callback_data="10mband")
        ],
        [
            InlineKeyboardButton(text="❌", callback_data="ochirish"),
            InlineKeyboardButton(text="⏩", callback_data="jonyga")
        ]
    ],
)

InBillie = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1billie"),
            InlineKeyboardButton(text="2", callback_data="2billie"),
            InlineKeyboardButton(text="3", callback_data="3billie"),
            InlineKeyboardButton(text="4", callback_data="4billie"),
            InlineKeyboardButton(text="5", callback_data="5billie")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="6billie"),
            InlineKeyboardButton(text="7", callback_data="7billie"),
            InlineKeyboardButton(text="8", callback_data="8billie"),
            InlineKeyboardButton(text="9", callback_data="9billie"),
            InlineKeyboardButton(text="10", callback_data="10billie")
        ],
        [
            InlineKeyboardButton(text="❌", callback_data="ochirish"),
            InlineKeyboardButton(text="⏩", callback_data="tentactionga")
        ]
    ],
)


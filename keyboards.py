from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_kb():
    builder = InlineKeyboardBuilder()

    builder.button(text="🔍 ТОП треки артиста", callback_data="search_tracks")
    builder.button(text="Караоке-режим", callback_data="karaoke_mode")

    builder.adjust(2)
    return builder.as_markup()

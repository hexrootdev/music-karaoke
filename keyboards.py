from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from yandex_parser import get_tracks_by_artist

def get_main_kb():
    builder = InlineKeyboardBuilder()

    builder.button(text="🔍 ТОП треки артиста", callback_data="search_tracks")
    builder.button(text="Караоке-режим", callback_data="karaoke_mode")

    builder.adjust(2)
    return builder.as_markup()

async def get_artists_kb(artist: str):
    builder = InlineKeyboardBuilder()

    tracks = await get_tracks_by_artist(artist=artist)
    for title, tid in tracks.items():
        builder.row(InlineKeyboardButton(text=title, url=f"https://music.yandex.ru/track/{tid}"))
    return builder.as_markup()

import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext as FSM
from aiogram.fsm.state import State, StatesGroup

from keyboards import get_main_kb
from yandex_parser import get_tracks_by_artist

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()

class SearchTrack(StatesGroup):
    artist_name = State()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}! Я эхо-бот на aiogram 3.x.", reply_markup=get_main_kb())

@dp.callback_query(F.data == "month_artists_top")
async def top_artists_month_handler(call: CallbackQuery):
    ...
#    artist = await get_tracks_by_artist
#    await call.message.answer(text=artist)
#    await call.answer()

@dp.callback_query(F.data == "search_tracks")
async def search_tracks_handler(call: CallbackQuery, state: FSM):
    await call.message.answer(f"Введите название исполнителя")
    await state.set_state(SearchTrack.artist_name)

@dp.message(SearchTrack.artist_name)
async def get_artist_name_handler(message: Message, state: FSM):
    artist = str(message.text)
    tracks = await get_tracks_by_artist(artist=artist)
    await message.answer(tracks + "\n")
    await state.clear()

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Токен твоего бота
TOKEN = "8937891004:AAFK2y4E6HZ0P7UEjA4dMCyJRVYYeun32ZY"
# Ссылка на мини-приложение (Netlify)
WEB_APP_URL = "https://chimerical-gecko-0e0834.netlify.app/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    lang_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")
        ]
    ])
    await message.answer(
        "🌐 Choose your language / Выберите язык:",
        reply_markup=lang_keyboard
    )

@dp.callback_query(lambda c: c.data.startswith("lang_"))
async def process_language(callback: types.CallbackQuery):
    lang = callback.data.split("_")[1]
    
    if lang == "ru":
        text = (
            "⚡️ **Добро пожаловать в Anomaly Drop!**\n\n"
            "Исследуй аномальный сектор, открывай контейнеры, собирай редкие артефакты и выводи их в TON.\n\n"
            "👇 *Жми кнопку ниже, чтобы запустить терминал и сделать первый дроп!*"
        )
        btn_text = "🚀 Запустить Anomaly Drop"
    else:
        text = (
            "⚡️ **Welcome to Anomaly Drop!**\n\n"
            "Explore the anomaly sector, open containers, collect rare artifacts, and withdraw them to TON.\n\n"
            "👇 *Click the button below to launch the terminal and make your first drop!*"
        )
        btn_text = "🚀 Launch Anomaly Drop"

    game_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=btn_text, web_app=WebAppInfo(url=WEB_APP_URL))]
    ])

    await callback.message.edit_text(text, reply_markup=game_keyboard, parse_mode="Markdown")
    await callback.answer()

async def main():
    print("Бот успешно запущен и ждет сообщения...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
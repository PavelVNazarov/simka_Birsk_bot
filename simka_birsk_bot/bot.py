# bot.py
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InputFile  # Импортируем InputFile
from config import API_TOKEN
from handlers import register_handlers

# Инициализация бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Регистрация обработчиков
register_handlers(dp, bot)

# Добавление обработчика для команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    chat_id = message.chat.id  # Получение chat_id
    logo = InputFile('images/logo.png')  # Используем InputFile для локального файла
    await bot.send_photo(chat_id, logo)  # Отправка изображения
    await message.reply("Добро пожаловать в салон услуг печати 'Симка'!", reply_markup=main_menu())

def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Услуги", "Прайс", "Контакты", "Режим работы"]
    keyboard.add(*buttons)
    return keyboard

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
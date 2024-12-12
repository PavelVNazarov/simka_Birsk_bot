# handlers.py
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile  # Импортируем InputFile для работы с локальными файлами

def register_handlers(dp: Dispatcher, bot):  # Функция для регистрации обработчиков
    @dp.message_handler(commands=['start'])
    async def send_welcome(message: types.Message):
        chat_id = message.chat.id
        logo = InputFile('images/logo.png')
        await bot.send_photo(chat_id, logo)
        await message.reply("Добро пожаловать в салон услуг печати 'Симка'!", reply_markup=main_menu())

    def main_menu():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Услуги", "Прайс", "Контакты", "Режим работы"]
        keyboard.add(*buttons)
        return keyboard

    @dp.message_handler(lambda message: message.text == "Услуги")
    async def send_services(message: types.Message):
        await message.reply("Печатный салон «Simka Birsk» - компания, которая предлагает цветную и ч/б печатную продукцию по доступным ценам!\n"
                             "1. Фотопечать, ксерокс\n"
                             "2. Распечатка ч/б и цветная\n"
                             "3. Печать визиток\n"
                             "4. Сканирование\n"
                             "5. Ламинирование\n"
                             "6. Фотомонтаж и реставрация фото\n"
                             "7. Брошюровка,\n"
                             "и многое другое.\n")

    @dp.message_handler(lambda message: message.text == "Прайс")
    async def send_price(message: types.Message):
        logo = InputFile('images/service.png')
        await bot.send_photo(message.chat.id, logo)

    @dp.message_handler(lambda message: message.text == "Режим работы")
    async def send_working_hours(message: types.Message):
        logo = InputFile('images/working_hours.png')
        await bot.send_photo(message.chat.id, logo)
        await message.reply("Принцип салона - быстрое оказание услуг!\n"
                             "1. Понедельник 9,00 - 19,00\n"
                             "2. Вторник 9,00 - 19,00\n"
                             "3. Среда 9,00 - 19,00\n"
                             "4. Четверг 9,00 - 19,00\n"
                             "5. Пятница 9,00 - 19,00\n"
                             "Выходные дни ")

    @dp.message_handler(lambda message: message.text == "Контакты")
    async def send_contact(message: types.Message):
        await message.reply("Контактная информация:\n"
                            "Телефон: +7 (927) 316-96-08\n"
                            "Telegram: [Нажмите для связи](https://t.me/79273169608)\n"
                            "Адрес: г. Бирск, ул. Интернациональная, д. 26\n"
                            "Ссылка на ВКонтакте: https://vk.com/simkabirsk?w=club139253477\n"
                            "WhatsApp: [Нажмите для связи](https://wa.me/79273169608)\n"
                            "Почта: mshamidanov@bk.ru\n"
                            "Все виды качественных печатных услуг в одном месте, по лучшим ценам!")

    @dp.message_handler(lambda message: True)  # Обработка любых текстовых сообщений
    async def handle_all_messages(message: types.Message):
        await message.reply("Ваше сообщение получено! Вот контакты для связи.")
        await send_contact(message)

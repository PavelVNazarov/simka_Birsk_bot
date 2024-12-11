# handlers.py
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile  # Импортируем InputFile для работы с локальными файлами

def register_handlers(dp: Dispatcher, bot):  # Функция для регистрации обработчиков
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
        logo = InputFile('images/service.png')  # Используем InputFile для локального файла
        await bot.send_photo(message.chat.id, logo)  # Отправка изображения вместо текста

    @dp.message_handler(lambda message: message.text == "Режим работы")
    async def send_price(message: types.Message):
        logo = InputFile('images/working_hours.png')  # Используем InputFile для локального файла
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
                            "Адрес: г. Бирск, ул. Интернациональная, д. 26\n"
                            "Ссылка на ВКонтакте: https://vk.com/simkabirsk?w=club139253477\n"
                            "WhatsApp: [Нажмите для связи](https://wa.me/79273169608)\n"  # Ссылка на WhatsApp
                            "Почта: mshamidanov@bk.ru\n"
                            "Все виды качественных печатных услуг в одном месте, по лучшим ценам!")  # Лозунг



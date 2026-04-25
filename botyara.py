# from aiogram import Bot, Dispatcher
# from aiogram.types import Message
# bot = Bot()
# dp = Dispatcher(bot)
# @dp.message(commands=['start'])
# async def cmd_start(message: Message):
#     await message.reply("Привет!")
#
# @dp.message()
# async def surname(message: Message):
#     your_surname = message.text
#     await message.reply(f'Вы ввели фамилию: {your_surname}')

# @dp.message_handler(lambda message: message.text in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
# async def class_selection(message: Message):
#     class_select = {
#         '1': 'Вы выбрали Класс 1',
#         '2': 'Вы выбрали Класс 2',
#         '3': 'Вы выбрали Класс 3',
#         '4': 'Вы выбрали Класс 4',
#         '5': 'Вы выбрали Класс 5',
#         '6': 'Вы выбрали Класс 6',
#         '7': 'Вы выбрали Класс 7',
#         '8': 'Вы выбрали Класс 8',
#         '9': 'Вы выбрали Класс 9',
#         '10': 'Вы выбрали Класс 10',
#         '11': 'Вы выбрали Класс 11'
#     }
#     await message.reply(class_select[message.text])
#
# @dp.message_handler()
# async def command(message: Message):
#     await message.reply("Пожалуйста, выбери класс, введя номер от 1 до 11.")
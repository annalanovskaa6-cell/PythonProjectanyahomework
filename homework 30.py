# import telebot
# TOKEN = 'ВАШ_ТОКЕН_ЗДЕСЬ'
# bot = telebot.TeleBot(TOKEN)
# @bot.message_handler(content_types=['photo', 'video', 'animation'])
# def handle_visual(message):
#     bot.reply_to(message, "Красивый визуальный контент!")
# @bot.message_handler(content_types=['voice', 'audio'])
# def handle_audio(message):
#     bot.reply_to(message, "Послушаю на досуге!")
# @bot.message_handler(content_types=['document'])
# def handle_document(message):
#     bot.reply_to(message, "Файл принят!")
# @bot.message_handler(content_types=['sticker'])
# def handle_sticker(message):
#     bot.reply_to(message, "Мой любимый стикер!")
# @bot.message_handler(func=lambda m: True)
# def handle_other(message):
#     bot.reply_to(message, "Записал")
# if __name__ == 'main':
#     bot.infinity_polling()



# import logging
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# TOKEN = "ВАШ_ТОКЕН_ЗДЕСЬ"
# logging.basicConfig(level=logging.INFO)
# def start(update: Update, context: CallbackContext):
#     lang = (update.effective_user.language_code or "").lower()
#     if lang.startswith("ru"):
#         text = "Привет! Добро пожаловать!"
#     elif lang.startswith("en"):
#         text = "Hello! Welcome!"
#     else:
#         text = "Hola!"
#         update.message.reply_text(text)
# def main():
#     updater = Updater(TOKEN, use_context=True)
#     dp = updater.dispatcher dp.add_handler(CommandHandler("start", start))
#     updater.start_polling()
#     updater.idle()
# if __name__ == "main":
#     main()



# from aiogram import Bot, Dispatcher, F, types
# import asyncio
# API_TOKEN = "ВАШ_ТОКЕН"
# bot = Bot(API_TOKEN)
# dp = Dispatcher()
# @dp.message(~(F.left_chat_member))
# async def handle_message(message: types.Message):
#     await message.reply("Сообщение получено!")
# if __name__ == "main":
#     asyncio.run(dp.start_polling(bot))
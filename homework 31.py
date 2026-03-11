# user_ids = []
# @dp.message(message: Message)
# def handle_message(message):
#     user_id = message.from_user.id
#     if user_id not in user_ids:
#         user_ids.append(user_id)
#         await message.answer(message, "Привет, новичек!")
#     else:
#         await message.answer(message, "Рад тебя снова видеть")
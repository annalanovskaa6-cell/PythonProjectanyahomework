# from aiogram import Router, types
# from aiogram.filters import Command
# from keyboards.inline import get_services_kb
# router = Router()
# @router.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer(
#         f"Добрый день, {message.from_user.full_name}! Выберите интересующую вас услугу:",
#         reply_markup=get_services_kb()
#     )
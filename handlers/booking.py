# from aiogram import Router, types, F
# from keyboards.inline import get_book_kb
# router = Router()
# @router.callback_query(F.data.startswith("service_"))
# async def show_service(callback: types.CallbackQuery):
#     service_name = ""
#     if callback.data == "service_haircut":
#         service_name = "Стрижка: создадим идеальный образ. Стоимость: 1500р."
#     elif callback.data == "service_manicure":
#         service_name = "Маникюр: классический и аппаратный. Стоимость: 1200р."
#     elif callback.data == "service_massage":
#         service_name = "Массаж: полное расслабление. Стоимость: 2500р."
#     await callback.message.edit_text(
#         text=service_name,
#         reply_markup=get_book_kb()
#     )
#     await callback.answer()
# @router.callback_query(F.data == "book_now")
# async def process_booking(callback: types.CallbackQuery):
#     await callback.message.answer("Вы успешно записаны! Наш менеджер свяжется с вами.")
#     await callback.message.edit_reply_markup(reply_markup=None)
#     await callback.answer()
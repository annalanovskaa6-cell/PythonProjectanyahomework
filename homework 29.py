# import asyncio
# async def calculate(x, delay):
#     await asyncio.sleep(delay)
#     return x ** 2
# tasks = [
#     calculate(2, 1),
#     calculate(3, 2),
#     calculate(4, 1)
# ]
# async def main():
#     results = await asyncio.gather(*tasks)
#     print("Результаты вычислений:")
#     for i, result in enumerate(results):
#         print(f"Число {i+1}: {result}")
# asyncio.run(main())                      #task 1



# import asyncio
# async def long_task():
#     print("Начало долгой задачи")
#     await asyncio.sleep(5)
#     print("Долгая задача завершена!")
# async def main():
#     task = asyncio.create_task(long_task())
#     await asyncio.sleep(2)
#     was_requested = task.cancel()
#     print("Запрошена отмена задачи: ", was_requested)
#     await asyncio.sleep(0)
#     if task.cancelled():
#         print("Задача была отменена:(")
#     elif task.done():
#         print("Задача успела завершиться!")
#     else:
#         print("Задача всё ещё выполняется...")
# asyncio.run(main())                            #task 2
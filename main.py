from unittest import skip
from aiogram import executor
from sys import argv
from init_db import create_tables

from bot_router import dp

if __name__ == "__main__":
    data = argv
    print(data)
    if data[1] == "migrate":       
        create_tables()
        print("Все таблицы созданы!")
    elif data[1] == "runbot":
        print("Бот запущен...")    
        executor.start_polling(dp, skip_updates=True) 
    else: 
        print("Напишите определенную команду!!!")
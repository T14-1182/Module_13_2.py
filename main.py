from aiogram import (Bot, Dispatcher, executor)
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7556016081:AAF4upKBzUACueEIgAlpK2aSqX6IB3Vzpsw'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text = ['/start'])
async def start_message(massage):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
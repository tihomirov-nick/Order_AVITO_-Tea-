from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage() # Выделение памяти для работы бота

bot = Bot(token=('TOKEN')) # Подключение к боту по токену 
dp = Dispatcher(bot, storage=storage) # Он будет обрабатывать входящие обновления
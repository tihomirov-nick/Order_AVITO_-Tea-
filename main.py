from aiogram.utils import executor
from create_bot import dp
from aiogram import types

async def on_startup(dp):
	print('Bot online...') # При запуске бота в консоль выыведется эта надпись
	await dp.bot.set_my_commands([
		types.BotCommand("start", "Запустить бота")]) # При использовании бота слева от клавиатуры добваляет меню с комамндами


from handlers import client # Импортирует из папки handlers файл client, в котором находится исполняемыый код

client.register_handlers_client(dp) # Регистрирует задействование хэндлеров при использовании бота в файле client.py

executor.start_polling(dp, skip_updates=True, on_startup=on_startup) # Строка, которая непосредственно запускает бота
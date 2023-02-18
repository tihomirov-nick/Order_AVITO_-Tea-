from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


############################################ БЛОК КОДА С КЛАВИАТУРАМИ ###############################################


main_btn = InlineKeyboardButton('Поехали!', callback_data='menu') # Инициализация с текстом 'Поехали!' и отправляемыми данными 'menu'
main_kb = InlineKeyboardMarkup().add(main_btn) # Инициализация клавиатуры с добавлением .add кнопки

back_btn = InlineKeyboardButton('Главное меню', callback_data='menu')

whatsapp_btn = InlineKeyboardButton(text='Telegram', url='https://t.me/derevyankina_a')

back_btn_low_1 = InlineKeyboardButton('Назад', callback_data='1')
back_btn_low_2 = InlineKeyboardButton('Назад', callback_data='2')
back_btn_low_3 = InlineKeyboardButton('Назад', callback_data='3')
back_btn_low_4 = InlineKeyboardButton('Назад', callback_data='4')

buy_btn_low_1 = InlineKeyboardButton('Заказать', callback_data='Заказать_1')
buy_btn_low_2 = InlineKeyboardButton('Заказать', callback_data='Заказать_2')
buy_btn_low_3 = InlineKeyboardButton('Заказать', callback_data='Заказать_3')
buy_btn_low_4 = InlineKeyboardButton('Заказать', callback_data='Заказать_4')

low_kb_1 = InlineKeyboardMarkup().add(back_btn_low_1, buy_btn_low_1).row(back_btn)
low_kb_2 = InlineKeyboardMarkup().add(back_btn_low_2, buy_btn_low_2).row(back_btn)
low_kb_3 = InlineKeyboardMarkup().add(back_btn_low_3, buy_btn_low_3).row(back_btn)
low_kb_4 = InlineKeyboardMarkup().add(back_btn_low_4, buy_btn_low_4).row(back_btn)

buy_kb_1 = InlineKeyboardMarkup().add(back_btn_low_1, whatsapp_btn).row(back_btn)
buy_kb_2 = InlineKeyboardMarkup().add(back_btn_low_2, whatsapp_btn).row(back_btn)
buy_kb_3 = InlineKeyboardMarkup().add(back_btn_low_3, whatsapp_btn).row(back_btn)
buy_kb_4 = InlineKeyboardMarkup().add(back_btn_low_4, whatsapp_btn).row(back_btn)

menu_btn_1 = InlineKeyboardButton('Ромашковый чай', callback_data='1')
menu_btn_2 = InlineKeyboardButton('Чай из гвоздики', callback_data='3')
menu_btn_3 = InlineKeyboardButton('Лавандовый чай', callback_data='2')
menu_btn_4 = InlineKeyboardButton('Чай из ягод черники', callback_data='4')
menu_kb = InlineKeyboardMarkup().add(menu_btn_1, menu_btn_2).row(menu_btn_3, menu_btn_4)

about_1_btn_1 = InlineKeyboardButton('Состав', callback_data='Состав_1')
about_1_btn_2 = InlineKeyboardButton('Цена/граммы', callback_data='Цена/граммы_1')
about_1_btn_3 = InlineKeyboardButton('Условия хранения', callback_data='Условия_1')
about_1_btn_4 = InlineKeyboardButton('Производитель', callback_data='Производитель_1')
about_1_kb = InlineKeyboardMarkup().add(about_1_btn_1, about_1_btn_2).row(about_1_btn_3, about_1_btn_4).row(back_btn)

about_2_btn_1 = InlineKeyboardButton('Состав', callback_data='Состав_2')
about_2_btn_2 = InlineKeyboardButton('Цена/граммы', callback_data='Цена/граммы_2')
about_2_btn_3 = InlineKeyboardButton('Условия хранения', callback_data='Условия_2')
about_2_btn_4 = InlineKeyboardButton('Производитель', callback_data='Производитель_2')
about_2_kb = InlineKeyboardMarkup().add(about_2_btn_1, about_2_btn_2).row(about_2_btn_3, about_2_btn_4).row(back_btn)

about_3_btn_1 = InlineKeyboardButton('Состав', callback_data='Состав_3')
about_3_btn_2 = InlineKeyboardButton('Цена/граммы', callback_data='Цена/граммы_3')
about_3_btn_3 = InlineKeyboardButton('Условия хранения', callback_data='Условия_3')
about_3_btn_4 = InlineKeyboardButton('Производитель', callback_data='Производитель_3')
about_3_kb = InlineKeyboardMarkup().add(about_3_btn_1, about_3_btn_2).row(about_3_btn_3, about_3_btn_4).row(back_btn)

about_4_btn_1 = InlineKeyboardButton('Состав', callback_data='Состав_4')
about_4_btn_2 = InlineKeyboardButton('Цена/граммы', callback_data='Цена/граммы_4')
about_4_btn_3 = InlineKeyboardButton('Условия хранения', callback_data='Условия_4')
about_4_btn_4 = InlineKeyboardButton('Производитель', callback_data='Производитель_4')
about_4_kb = InlineKeyboardMarkup().add(about_4_btn_1, about_4_btn_2).row(about_4_btn_3, about_4_btn_4).row(back_btn)


############################################ БЛОК КОДА С ФУНКЦИЯМИ, КОТОРЫЕ ВЫЗЫВАЮТСЯ КОГДА В ХЭГДЛЕР ПОПАДАЕТ НУЖНОЕ ЗНАЧЕНИЕ ###############################################


async def start_command(message: types.Message): # Функция, которая отправляет пользователю сообщение при задействовании соответствующего хэндлера
    await bot.send_message(message.from_user.id, # Первый передаваемый параметр отвечает за то, кому будет отправлено сообщение >>> from_user.id означает, что сообщение отправится по id пользователя, который отправли прошлое сообщение
                           text='Приветствую тебя мой дорогой друг!\nЯ чат-бот Таисия Васильевна. И сейчас я расскажу вам о самом вкусном чае.\n\nНажимите на кнопку "ПОЕХАЛИ" и я покажу вам нашу продукцию', # Текст отправляемого сообщения
                           reply_markup=main_kb) # Параметр, который вызывает клавиатуру под сообщением строка 10


async def show_products(callback_query: types.CallbackQuery): # Функция, которая улавливает данные от пользователя, по которым она должна начать работу, в этом случае данные поступят от клавиатуры main_kb(строка 10) >>> callback_data='menu' именно на данные 'menu' она откликается
    await bot.answer_callback_query(callback_query.id)
    photo = open("E:/Python/TEE_BOT/tee.jpg", 'rb') # Вызываем фото из папки, в которой расположен бот
    await bot.send_photo(callback_query.message.chat.id, photo, caption='Ассортимент чая', reply_markup=menu_kb) # Отправка фото (bot.send_photo), куда (message.chat.id) - в чат с таким же id, как и сообщение, которое передало в это функцию данные 'menu', что отправляем (photo), с подписью (Ассортимент чая), с клавиатурой (menu_kb)


async def tee_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    photo = open("E:/Python/TEE_BOT/1.jpg", 'rb')
    await bot.send_photo(callback_query.message.chat.id, photo, caption='Ромашковый чай', reply_markup=about_1_kb)


async def tee_2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    photo = open("E:/Python/TEE_BOT/2.jpg", 'rb')
    await bot.send_photo(callback_query.message.chat.id, photo, caption='Лавандовый чай', reply_markup=about_2_kb)


async def tee_3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    photo = open("E:/Python/TEE_BOT/3.jpg", 'rb')
    await bot.send_photo(callback_query.message.chat.id, photo, caption='Чай из гвоздики', reply_markup=about_3_kb)


async def tee_4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    photo = open("E:/Python/TEE_BOT/4.jpg", 'rb')
    await bot.send_photo(callback_query.message.chat.id, photo, caption='Чай из ягод черники', reply_markup=about_4_kb)


async def сomposition_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Состав: ромашка, имбирь, мята, цедра лимона, душица, тысячелистник, иван-чай, шиповник, брусника, мелисса и череда, зелёный чай',
                           reply_markup=low_kb_1)


async def price_mass_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, text=f"{'<b>'}Цена/граммы:{'</b>'}\n85р./40гр.",
                           parse_mode='HTML', reply_markup=low_kb_1)


async def conditions_of_storage_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text=f"{'<b>'}Условия хранения:{'</b>'}\nНеобходимо хранить в сухом, чистом, хорошо вентилируемом помещении, не имеющем посторонних запахов, при относительной влажности воздуха не более 75%. Товар не должен подвергаться прямому воздействию солнечного света и влаги.",
                           parse_mode='HTML', reply_markup=low_kb_1)


async def producer_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Изготовитель: ООО «Butterfley”. Место нахождения: Россия, 187024, г. Москва, ул. 800-летия Москвы, д. 28.\nАдрес производства: Россия, 404620, г. Ленинск, ул. Ленина, д.22.',
                           reply_markup=low_kb_1)


async def сomposition_2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Состав: лаванда, плоды и лепестки шиповника, сушенные яблоки, имбирь, листья мяты, зелёный чай',
                           reply_markup=low_kb_2)


async def price_mass_2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, text=f"{'<b>'}Цена/граммы:{'</b>'}\n85р./40гр.",
                           parse_mode='HTML', reply_markup=low_kb_2)


async def conditions_of_storage_2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text=f"{'<b>'}Условия хранения:{'</b>'}\nНеобходимо хранить в сухом, чистом, хорошо вентилируемом помещении, не имеющем посторонних запахов, при относительной влажности воздуха не более 75%. Товар не должен подвергаться прямому воздействию солнечного света и влаги.",
                           parse_mode='HTML', reply_markup=low_kb_2)


async def producer_2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Изготовитель: ООО «Butterfley”. Место нахождения: Россия, 187024, г. Москва, ул. 800-летия Москвы, д. 28.\nАдрес производства: Россия, 404620, г. Ленинск, ул. Ленина, д.22.',
                           reply_markup=low_kb_2)


async def сomposition_3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Состав: гвоздика, чебрец, корица, зверобой, листья брусники, плоды шиповника, корень валерианы, зелёный чай',
                           reply_markup=low_kb_3)


async def price_mass_3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, text=f"{'<b>'}Цена/граммы:{'</b>'}\n85р./40гр.",
                           parse_mode='HTML', reply_markup=low_kb_3)


async def conditions_of_storage_3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text=f"{'<b>'}Условия хранения:{'</b>'}\nНеобходимо хранить в сухом, чистом, хорошо вентилируемом помещении, не имеющем посторонних запахов, при относительной влажности воздуха не более 75%. Товар не должен подвергаться прямому воздействию солнечного света и влаги.",
                           parse_mode='HTML', reply_markup=low_kb_3)


async def producer_3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Изготовитель: ООО «Butterfley”. Место нахождения: Россия, 187024, г. Москва, ул. 800-летия Москвы, д. 28.\nАдрес производства: Россия, 404620, г. Ленинск, ул. Ленина, д.22.',
                           reply_markup=low_kb_3)


async def сomposition_4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Состав: ягоды черники, цедра апельсина, сушенные яблоки, листья смородины, листья брусники и земляники, ягоды малины, зелёный чай',
                           reply_markup=low_kb_4)


async def price_mass_4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id, text=f"{'<b>'}Цена/граммы:{'</b>'}\n85р./40гр.",
                           parse_mode='HTML', reply_markup=low_kb_4)


async def conditions_of_storage_4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text=f"{'<b>'}Условия хранения:{'</b>'}\nНеобходимо хранить в сухом, чистом, хорошо вентилируемом помещении, не имеющем посторонних запахов, при относительной влажности воздуха не более 75%. Товар не должен подвергаться прямому воздействию солнечного света и влаги.",
                           parse_mode='HTML', reply_markup=low_kb_4)


async def producer_4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Изготовитель: ООО «Butterfley”. Место нахождения: Россия, 187024, г. Москва, ул. 800-летия Москвы, д. 28.\nАдрес производства: Россия, 404620, г. Ленинск, ул. Ленина, д.22.',
                           reply_markup=low_kb_4)


async def buy_1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Заказать чай', reply_markup=buy_kb_1)


async def buy_2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Заказать чай', reply_markup=buy_kb_2)


async def buy_3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Заказать чай', reply_markup=buy_kb_3)


async def buy_4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.message.chat.id,
                           text='Заказать чай', reply_markup=buy_kb_4)


############################################ БЛОК КОДА С ХЭНДЛЕРАМИ ###############################################


def register_handlers_client(dp: Dispatcher):

    # Хэндлер, который реагирует на команду /start и вызывает ф-ию start_command()
    dp.register_message_handler(start_command, commands=['start'])

    # Хэндлер, который реагирует на данные 'menu' и вызывает ф-ию show_products(), все остальные хэндлеры работают по такому же принципу
    dp.register_callback_query_handler(show_products, lambda c: c.data == 'menu')
    dp.register_callback_query_handler(tee_1, lambda c: c.data == '1')
    dp.register_callback_query_handler(tee_2, lambda c: c.data == '2')
    dp.register_callback_query_handler(tee_3, lambda c: c.data == '3')
    dp.register_callback_query_handler(tee_4, lambda c: c.data == '4')

    dp.register_callback_query_handler(сomposition_1, lambda c: c.data == 'Состав_1')
    dp.register_callback_query_handler(price_mass_1, lambda c: c.data == 'Цена/граммы_1')
    dp.register_callback_query_handler(conditions_of_storage_1, lambda c: c.data == 'Условия_1')
    dp.register_callback_query_handler(producer_1, lambda c: c.data == 'Производитель_1')

    dp.register_callback_query_handler(сomposition_2, lambda c: c.data == 'Состав_2')
    dp.register_callback_query_handler(price_mass_2, lambda c: c.data == 'Цена/граммы_2')
    dp.register_callback_query_handler(conditions_of_storage_2, lambda c: c.data == 'Условия_2')
    dp.register_callback_query_handler(producer_2, lambda c: c.data == 'Производитель_2')

    dp.register_callback_query_handler(сomposition_3, lambda c: c.data == 'Состав_3')
    dp.register_callback_query_handler(price_mass_3, lambda c: c.data == 'Цена/граммы_3')
    dp.register_callback_query_handler(conditions_of_storage_3, lambda c: c.data == 'Условия_3')
    dp.register_callback_query_handler(producer_3, lambda c: c.data == 'Производитель_3')

    dp.register_callback_query_handler(сomposition_4, lambda c: c.data == 'Состав_4')
    dp.register_callback_query_handler(price_mass_4, lambda c: c.data == 'Цена/граммы_4')
    dp.register_callback_query_handler(conditions_of_storage_4, lambda c: c.data == 'Условия_4')
    dp.register_callback_query_handler(producer_4, lambda c: c.data == 'Производитель_4')

    dp.register_callback_query_handler(buy_1, lambda c: c.data == 'Заказать_1')
    dp.register_callback_query_handler(buy_2, lambda c: c.data == 'Заказать_2')
    dp.register_callback_query_handler(buy_3, lambda c: c.data == 'Заказать_3')
    dp.register_callback_query_handler(buy_4, lambda c: c.data == 'Заказать_4')
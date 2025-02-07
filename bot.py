from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


ADMIN = ['6888643375']


bot = Bot(token='7692626473:AAEgJxf5PS_RG0_geBIqP3V8UU1uKlzmwl8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler(commands=['adm'])
async def admins(message: types.Message):
    user_id = message.from_user.id
    if user_id not in ADMIN:
        await message.answer('Вы админ')
    else: 
        await message. answer('Вы хуесос без админки')

@dp.message_handler(commands=['lol'])
async def lol(message: types.Message):
    Keyboard = types.InlineKeyboardMarkup()
    Keyboard.add(types.InlineKeyboardButton(text='лолошный лол?', callback_data = 'mda'))
    await message.anwer('ЕТА ЧО ТАКОЕ??', reply_markup = Keyboard)

@dp.callback_query_handler(text='mda')
async def mda(call: types.CallbackQuery):
    await call.message.answer('ТУДА СЮДА И БАГАЧЬ ЕЕЕЕ')



@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)




if __name__ == '__main__':
    executor.start_polling(dp)

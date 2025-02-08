from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3 

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER,
    name TEXT,
    balance TEXT
)''')


                   

async def getbalance(message):
    user_id = message.from_user.id
    cursor.execute('SELECT name, balance FROM users WHERE user_id = ?', (user_id,))
    i = cursor.fetchone()
    name, balance = i
    return name, balance


ADMIN = ['6888643375']


bot = Bot(token='7692626473:AAEgJxf5PS_RG0_geBIqP3V8UU1uKlzmwl8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def register_users(message):
    user_id = message.from_user.id

    cursor.execute('SELECT name FROM users WHERE user_id = ?', (user_id,))
    ex = cursor.fetchone()

    if not ex:
        cursor.execute('INSERT INTO users (user_id, name, balance) VALUES (?, ?, ?)', (user_id, 'Игрок', 1000))
        conn.commit()
        await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler(commands=['balance'])
async def balance(message: types.Message):
    name, balance = await getbalance(message)
    await message.answer(f'Ваш баланс {balance}', parse_mode='html')

@dp.message_handler(commands=['click'])
async def click(message: types.Message):
    user_id = message.from_user.id
    cursor.execute('UPDATE users SET balance = balance + ? WHERE user_id', (1, user_id))
    await message.answer(f'Вы заработали + 1 рубаааль', parse_mode='html')


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
    await message.answer('ЕТА ЧО ТАКОЕ??', reply_markup = Keyboard)

@dp.callback_query_handler(text='mda')
async def mda(call: types.CallbackQuery):
    await call.answer(text = 'ТУДА СЮДА И БАГАЧЬ ЕЕЕЕ', show_alert=True)




if __name__ == '__main__':
    executor.start_polling(dp)

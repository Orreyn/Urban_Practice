from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import crud_functions as cf

cf.get_all_products()

api = ''
lutch = Bot(token=api)
dp = Dispatcher(lutch, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
count = KeyboardButton(text='Рассчитать')
info = KeyboardButton(text='Информация')
buy = KeyboardButton(text='Купить')
kb.add(count)
kb.add(info)
kb.add(buy)

ikb = InlineKeyboardMarkup()
counter = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formuls = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb.add(counter)
ikb.add(formuls)

byikb = InlineKeyboardMarkup()
p1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
p2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
p3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
p4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')

byikb.row(p1, p2, p3, p4)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ikb)


@dp.message_handler(text=['Информация'])
async def info(message, state):
    await message.answer('Информация о боте')


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i in range(1,5):
        with open(f'{i}.png', 'rb') as img:
            await message.answer(cf.get_all_products())
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=byikb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(f'Вы успешно приобрели продукт!')


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calories')
async def set_age(call, state):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f'Ваша норма калорий {(int(data["weight"]) * 10) + (int(data["growth"]) * 6.25) - (int(data["age"]) * 5) - 161}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

get_buying_list()

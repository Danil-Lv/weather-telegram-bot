from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from dotenv import load_dotenv
import os
from weather_request import get_weather
from keyboard import kb

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class CityStatesGroup(StatesGroup):
    city = State()


async def on_startup(_):
    print('Bot is active')


@dp.message_handler(commands=['start'])
async def start_foo(message: types.Message):
    await message.answer(text='In this bot you can get the weather in any city.', reply_markup=kb)
    await message.delete()


#
#
@dp.message_handler(state=CityStatesGroup.city)
async def get_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
        city = data['city']
    try:
        await message.answer(f'The weather in {city.title()}: {get_weather(city)["main"]["temp"]}℃')
    except:
        await message.answer('Please enter the city name correctly.')


@dp.message_handler(text='Get weather')
async def weather_foo(message: types.Message):
    await message.answer('Enter the names of the cities, the bot will send the weather.')
    await CityStatesGroup.city.set()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

import os
import config
from markup import Keyboard
from utils import Utils
from aiogram import Bot,Dispatcher,types,executor
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile


class Bot:
    bot = Bot(token=config.TOKEN, parse_mode="HTML")
    dp = Dispatcher(bot,storage=MemoryStorage())
    kb = Keyboard()
    utils = Utils()


    def __init__(self) -> None:
        executor.start_polling(Bot.dp, skip_updates=True)


    @dp.message_handler(commands = ['start'],state=None)
    async def start(message: types.Message):
        await message.answer('Бот запущен.',reply_markup=Bot.kb.keyboard())


    @dp.message_handler(Text(equals=kb.button(0)))
    async def make_order_for_number(message: types.Message, state: FSMContext):
        doc_name = Bot.utils.get_current_json_task()
        await Bot.bot.send_document(message.from_user.id,InputFile(doc_name, filename=doc_name),reply_markup=Bot.kb.keyboard())
        os.remove(doc_name)

    
    @dp.message_handler(Text(equals=kb.button(1)))
    async def make_order_for_number(message: types.Message, state: FSMContext):
        pass


if __name__=='__main__':
    bot = Bot()
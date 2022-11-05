from aiogram import types
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentType


class Keyboard:
    def __init__(self) -> None:
        self.main_buttons = ['Печать текущего дня','Печать по дате']

    def keyboard(self):
        keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard_main.add(*self.main_buttons)
        return keyboard_main

    def button(self, number):
        return self.main_buttons[number]
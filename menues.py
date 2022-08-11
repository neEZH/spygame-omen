from telebot import types


def start_create_add():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_start = types.KeyboardButton('Start')
    button_create = types.KeyboardButton('Create')
    menu.add(button_create, button_start)
    return menu

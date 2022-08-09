from telebot import types

def create_join_add():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_create = types.KeyboardButton('Create')
    button_join = types.KeyboardButton('Join')
    button_add = types.KeyboardButton('Add place')
    menu.add(button_create, button_join, button_add)
    return menu


def start_back():
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_start = types.KeyboardButton('Start')
    button_back = types.KeyboardButton('Back')
    menu.add(button_start, button_back)
    return menu

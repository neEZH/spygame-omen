import os
import menues as m
import telebot
# from telebot import types

tbot = telebot.TeleBot(os.environ['tbotToken'])


@tbot.message_handler(commands=["start"])
def start(message):
    tbot.send_message(message.chat.id, "hello there", reply_markup=m.create_join_add())


@tbot.message_handler(regexp="")
def any_msg(message):
    print(message.text.encode("utf-8"))
    tbot.send_message(message.chat.id, "\U0001F600")

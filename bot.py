import os
import menues as m
import telebot
import spyBot as spy
# from telebot import types

tbot = telebot.TeleBot(os.environ['tbotToken'])


@tbot.message_handler(commands=["start"])
def start(message):
    # reply = spy.new_player(message.from_user.id, message.from_user.username, message.from_user.is_bot)
    tbot.send_message(message.chat.id, "reply")


@tbot.message_handler(regexp="")
def any_msg(message):
    print(message.text.encode("utf-8"))
    tbot.send_message(message.chat.id, "\U0001F600")

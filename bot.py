import os
import menues as m
import telebot
import spyBot as spy

# from telebot import types

tbot = telebot.TeleBot(os.environ['tbotToken'])


@tbot.message_handler(commands=["start"])
def start(message):
    reply = spy.new_player(message.from_user.id, message.from_user.username, message.from_user.is_bot)
    tbot.send_message(message.chat.id, reply, reply_markup=m.start_create_add())


@tbot.message_handler(regexp="Create")
def create(message):
    reply = spy.new_room(message.from_user.id)
    tbot.send_message(message.chat.id, reply, reply_markup=m.start_create_add(), parse_mode="MarkdownV2")


@tbot.message_handler(regexp="\A\w{6}$")
def join(message):
    reply = spy.join_room(message.from_user.id, message.text)
    tbot.send_message(message.chat.id, reply, reply_markup=m.start_create_add())


@tbot.message_handler(commands=["addplace"])
def add_place(message):
    tbot.reply_to(message, "type place next to command, like \"/addplace some place\"")


@tbot.message_handler(regexp="")
def any_msg(message):
    print(message.text.encode("utf-8"))
    tbot.send_message(message.chat.id, "\U0001F600")

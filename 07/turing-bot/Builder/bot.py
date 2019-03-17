#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import logging
from Keyboard import Keyboard
from telebot import types

bot = telebot.TeleBot("708293438:AAEHbWJK0UTwMddBCuc-9C6t3ia1txcmu44")

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(
        message.chat.id, "Hello, Turing!", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    show_builder(message.chat.id)


def show_builder(chat_id):
    keyboard = Keyboard()
    keyboard.addButtons(["Test1", "Test2"])
    keyboard.setOneTimeKeyboard(True)
    keyboard.setRowWidth(2)
    keyboard.shouldKeyboardBeResized(True)
    bot.send_message(chat_id, "Choose one letter:",
                     reply_markup=keyboard.getResult())


if __name__ == '__main__':
    bot.polling()

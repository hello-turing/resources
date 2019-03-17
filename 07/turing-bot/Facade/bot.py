#! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import logging
from Facade import BotFacade

facade = BotFacade()
bot = facade.getBot()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, "Hello, Turing!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == '__main__':
    facade.startBot()

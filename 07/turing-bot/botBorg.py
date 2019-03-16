#! /usr/bin/env python
# -*- coding: utf-8 -*-
import threading

import telebot
import logging
from UserBorg import UserBorg

bot = telebot.TeleBot("708293438:AAEHbWJK0UTwMddBCuc-9C6t3ia1txcmu44")

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, "Howdy, how are you doing?")


def printit():
  threading.Timer(5.0, printit).start()
  print ("Hello, World!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    rm1 = UserBorg()
    rm2 = UserBorg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    rm2.state = 'Zombie'

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))

    print('rm1 id: {0}'.format(id(rm1)))
    print('rm2 id: {0}'.format(id(rm2)))

    rm3 = UserBorg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print('rm3: {0}'.format(rm3))
    bot.get_me()


if __name__ == '__main__':
    bot.polling()
    printit()
 


import telebot

bot = telebot.TeleBot("708293438:AAEHbWJK0UTwMddBCuc-9C6t3ia1txcmu44")


class UserBorg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state

    def getAllUserData(self):
        return bot.get_me()

    def getFirstName(self):
        return bot.get_me().first_name

import telebot
import logging
from telebot import apihelper


class _Logger(object):
    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger(__name__)


class _Bot(object):
    def __init__(self):
        self.bot = telebot.TeleBot(
            "708293438:AAEHbWJK0UTwMddBCuc-9C6t3ia1txcmu44")
        # set webhook
        # self.bot.set_webhook(url="http://example.com",
        #                certificate=open('mycert.pem'))
        # unset webhook
        # self.bot.remove_webhook()

        # proxy
        # apihelper.proxy = {'http':'http://10.10.1.10:3128'}

    def startPolling(self):
        self.bot.polling()

    def getBot(self):
        return self.bot


class BotFacade(object):
    def __init__(self):
        self.bot = _Bot()
        self.logger = _Logger()

    def startBot(self):
        self.bot.startPolling()

    def getBot(self):
        return self.bot.getBot()

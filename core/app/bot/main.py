from django.conf import settings
from app.bot.db import adduser

from telebot import TeleBot
from app.bot.markup import startMarkup
from telebot import logger


bot = TeleBot(token=settings.BOT_TOKEN, parse_mode='HTML')
logger.setLevel(settings.LOG_LEVEL)

@bot.message_handler(commands=['start'])
def start(msg):
    adduser(msg)
    markup = startMarkup()
    bot.send_message(msg.chat.id, 'mq', reply_markup=markup)

@bot.message_handler(commands=['admin'])
def adminPanel(msg):
    pass

@bot.callback_query_handler(func=lambda call: True)
def startButtons(call):
    if call.data == 'askQuestion':
        msg = bot.send_message(call.message.chat.id, "Задай вопрос")
        bot.register_next_step_handler(msg, sendQuestion)
    elif call.data == 'profileData':
        pass
    elif call.data == 'questionList':
        pass
    elif call.data == 'notificationsSubscription':
        pass

def sendQuestion(msg):
    bot.reply_to(msg, "Вопрос сохранён")
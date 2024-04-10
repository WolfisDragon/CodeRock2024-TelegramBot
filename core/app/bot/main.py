from django.conf import settings
from app.bot.db import adduser, addQuestion, getprofile, getQuestion, addAnswer

from telebot import TeleBot
from app.bot.markup import startMarkup, answerQustion
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
        profile = getprofile(call.message)
        bot.send_message(call.message.chat.id, f"Ваш профиль\nID {profile[0]}\nUsername @{profile[1]}")
    elif call.data == 'questionList':
        qustions = getQuestion()
        answerMarkup = answerQustion()
        for qustion in qustions:
            bot.send_message(call.message.chat.id, qustion, reply_markup=answerMarkup)
    elif call.data == 'notificationsSubscription':
        pass
    elif call.data == 'answer':
        msg = bot.send_message(call.message.chat.id, f'Введите ответ на вопрос "{call.message.text}"')
        bot.register_next_step_handler(msg, sendAnswer, call.message.text)

def sendQuestion(msg):
    try:
        addQuestion(msg)
        bot.reply_to(msg, "Вопрос сохранён")

    except Exception as e:
        bot.reply_to(msg, 'Error')

def sendAnswer(msg, callmsg):
    try:
        addAnswer(msg, callmsg)
        bot.reply_to(msg, 'Ответ записан')
    except Exception as e:
        bot.reply_to(msg, 'Error')
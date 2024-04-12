from django.conf import settings
from app.bot.db import adduser, addQuestion, getprofile, getQuestion, addAnswer, viewAnswer, checkLog, checkPass, viewQuestionsToModerate, viewAnswersToModerate, getQ

from telebot import TeleBot
from app.bot.markup import startMarkup, answerQuestion, adminPanelMarkup, moderateQuestionMarkup, moderateAnswerMarkup
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
    bot.send_message(msg.chat.id, "Введите ваш логин:")
    bot.register_next_step_handler(msg, checkLogin)

@bot.callback_query_handler(func=lambda call: True)
def startButtons(call):
    if call.data == 'askQuestion':
        msg = bot.send_message(call.message.chat.id, "Задай вопрос")
        bot.register_next_step_handler(msg, sendQuestion)
    elif call.data == 'profileData':
        profile = getprofile(call.message)
        bot.send_message(call.message.chat.id, f"Ваш профиль\nID {profile[0]}\nUsername @{profile[1]}")
    elif call.data == 'questionList':
        questions = getQuestion()
        if questions == []:
            bot.send_message(call.message.chat.id, 'Нет активных вопросов')
        else:
            answerMarkup = answerQuestion()
            for question in questions:
                bot.send_message(call.message.chat.id, question, reply_markup=answerMarkup)
    elif call.data == 'notificationsSubscription':
        pass
    elif call.data == 'answer':
        msg = bot.send_message(call.message.chat.id, f'Введите ответ на вопрос "{call.message.text}"')
        bot.register_next_step_handler(msg, sendAnswer, call.message.text)

    elif call.data == 'viewAnswer':
        answers = viewAnswer(call.message.text)
        if answers == []:
            bot.send_message(call.message.chat.id, 'Нет ответов')
        else:
            for answer in answers:
                bot.send_message(call.message.chat.id, f'Ответ: {answer}')
            
    elif call.data == 'questionsModerate':
        questions = viewQuestionsToModerate()
        if questions == []:
            bot.send_message(call.message.chat.id, 'Нет вопросов')
        else:
            for q in questions:
                bot.send_message(call.message.chat.id, f'Вопрос: {q}', reply_markup=moderateQuestionMarkup())

    elif call.data == 'answersModerate':
        answers = viewAnswersToModerate()
        if answers == []:
            bot.send_message(call.message.chat.id, 'Нет ответов')
        else:
            for answer in answers:
                q = getQ(answer)
                bot.send_message(call.message.chat.id, f'Вопрос: {q}, ответ: {answer}', reply_markup=moderateAnswerMarkup())

    elif call.data == 'approveQuestion':
        pass

    elif call.data == 'deleteQuestion':
        pass

    elif call.data == 'approveAnswer':
        pass

    elif call.data == 'deleteAnswer':
        pass

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

def checkPassword(msg):
    try:
        if checkPass(msg):
            bot.reply_to(msg, 'Успешная авторизация!')
            adminMarkup = adminPanelMarkup()
            bot.send_message(msg.chat.id, "Админ-панель:", reply_markup=adminMarkup)
        else:
            bot.reply_to(msg, 'Неверный пароль')
    except Exception as e:
        bot.reply_to(msg, 'Error')

def checkLogin(msg):
    try:
        if checkLog(msg):
            bot.reply_to(msg, 'Введите пароль:')
            bot.register_next_step_handler(msg, checkPassword)
        else:
            bot.reply_to(msg, 'Неверный логин')
    except Exception as e:
        bot.reply_to(msg, 'Error')
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def startMarkup():
    markups = InlineKeyboardMarkup()
    markups.add(InlineKeyboardButton('задать вопрос', callback_data = 'askQuestion'))
    markups.add(InlineKeyboardButton('профиль', callback_data = 'profileData'))
    markups.add(InlineKeyboardButton('список вопросов', callback_data = 'questionList'))
    markups.add(InlineKeyboardButton('рассылка', callback_data = 'notificationsSubscription'))
    return markups

def answerQustion():
    answerMarkup = InlineKeyboardMarkup()
    answerMarkup.add(InlineKeyboardButton('ответить на вопрос', callback_data='answer'))
    return answerMarkup
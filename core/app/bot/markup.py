from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def startMarkup():
    markups = InlineKeyboardMarkup()
    markups.add(InlineKeyboardButton('задать вопрос', callback_data = 'askQuestion'))
    markups.add(InlineKeyboardButton('профиль', callback_data = 'profileData'))
    markups.add(InlineKeyboardButton('список вопросов', callback_data = 'questionList'))
    markups.add(InlineKeyboardButton('рассылка', callback_data = 'notificationsSubscription'))
    return markups

def answerQuestion():
    answerMarkup = InlineKeyboardMarkup()
    answerMarkup.add(InlineKeyboardButton('посмотреть ответы', callback_data='viewAnswer'))
    answerMarkup.add(InlineKeyboardButton('ответить на вопрос', callback_data='answer'))
    return answerMarkup
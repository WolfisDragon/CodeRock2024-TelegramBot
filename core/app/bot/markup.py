from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def startMarkup():
    markups = InlineKeyboardMarkup()
    markups.add(InlineKeyboardButton('задать вопрос', callback_data = 'askQuestion'))
    markups.add(InlineKeyboardButton('профиль', callback_data = 'profileData'))
    markups.add(InlineKeyboardButton('список вопросов', callback_data = 'questionList'))
    return markups

def answerQuestion():
    answerMarkup = InlineKeyboardMarkup()
    answerMarkup.add(InlineKeyboardButton('посмотреть ответы', callback_data='viewAnswer'))
    answerMarkup.add(InlineKeyboardButton('ответить на вопрос', callback_data='answer'))
    return answerMarkup

def adminPanelMarkup():
    adminMarkup = InlineKeyboardMarkup()
    adminMarkup.add(InlineKeyboardButton('Модерация вопросов', callback_data='questionsModerate'))
    adminMarkup.add(InlineKeyboardButton('Модерация ответов', callback_data='answersModerate'))
    return adminMarkup

def moderateQuestionMarkup():
    moderateMarkup = InlineKeyboardMarkup()
    moderateMarkup.add(InlineKeyboardButton('одобрить', callback_data = 'approveQuestion'))
    moderateMarkup.add(InlineKeyboardButton('удалить', callback_data = 'deleteQuestion'))
    return moderateMarkup

def moderateAnswerMarkup():
    moderateMarkup = InlineKeyboardMarkup()
    moderateMarkup.add(InlineKeyboardButton('одобрить', callback_data = 'approveAnswer'))
    moderateMarkup.add(InlineKeyboardButton('удалить', callback_data = 'deleteAnswer'))
    return moderateMarkup
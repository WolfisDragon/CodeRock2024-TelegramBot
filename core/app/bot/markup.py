from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def startMarkup():
    markups = InlineKeyboardMarkup()
    markups.add(InlineKeyboardButton('Задать вопрос', callback_data = 'askQuestion'))
    markups.add(InlineKeyboardButton('Профиль', callback_data = 'profileData'))
    markups.add(InlineKeyboardButton('Список вопросов', callback_data = 'questionList'))
    return markups

def answerQuestion():
    answerMarkup = InlineKeyboardMarkup()
    answerMarkup.add(InlineKeyboardButton('Посмотреть ответы', callback_data='viewAnswer'))
    answerMarkup.add(InlineKeyboardButton('Ответить на вопрос', callback_data='answer'))
    return answerMarkup

def adminPanelMarkup():
    adminMarkup = InlineKeyboardMarkup()
    adminMarkup.add(InlineKeyboardButton('Модерация вопросов', callback_data='questionsModerate'))
    adminMarkup.add(InlineKeyboardButton('Модерация ответов', callback_data='answersModerate'))
    return adminMarkup

def moderateQuestionMarkup():
    moderateMarkup = InlineKeyboardMarkup()
    moderateMarkup.add(InlineKeyboardButton('Одобрить', callback_data = 'approveQuestion'))
    moderateMarkup.add(InlineKeyboardButton('Удалить', callback_data = 'deleteQuestion'))
    return moderateMarkup

def moderateAnswerMarkup():
    moderateMarkup = InlineKeyboardMarkup()
    moderateMarkup.add(InlineKeyboardButton('Одобрить', callback_data = 'approveAnswer'))
    moderateMarkup.add(InlineKeyboardButton('Удалить', callback_data = 'deleteAnswer'))
    return moderateMarkup
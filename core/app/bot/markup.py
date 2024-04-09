from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
async def startmarkup():
    markups = InlineKeyboardMarkup()
    markups.add(InlineKeyboardButton('задать вопрос', callback_data = 'questionData'))
    markups.add(InlineKeyboardButton('профиль', callback_data = 'profileData'))
    markups.add(InlineKeyboardButton('список вопросов', callback_data = 'questionList'))
    markups.add(InlineKeyboardButton('рассылка', callback_data = 'notificationsSubscription'))
    return markups
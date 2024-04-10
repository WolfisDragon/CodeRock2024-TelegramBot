from django.conf import settings

from telebot.async_telebot import AsyncTeleBot
from app.bot.markup import startMarkup
from telebot import logger


bot = AsyncTeleBot(token=settings.BOT_TOKEN, parse_mode='HTML')
logger.setLevel(settings.LOG_LEVEL)

@bot.message_handler(commands=['start'])
async def start(msg):
    markup = await startMarkup()
    await bot.send_message(msg.chat.id, 'mq', reply_markup=markup)

@bot.message_handler(commands=['admin'])
async def adminPanel(msg):
    pass

@bot.callback_query_handler(func=lambda call: True)
async def startButtons(call):
    if call.data == 'questionData':
        pass 
    elif call.data == 'profileData':
        pass
    elif call.data == 'questionList':
        pass
    elif call.data == 'notificationsSubscription':
        pass
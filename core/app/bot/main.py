import telebot
from telebot.async_telebot import AsyncTeleBot
from app.bot.markup import startmarkup

bot = AsyncTeleBot('6543777887:AAFgXq6i6IM8okrRT8057UMlOBFtZBlyUes')

@bot.message_handler(commands=['start'])
async def start(msg):
    markup = await startmarkup()
    await bot.send_message(msg.chat.id, 'mq', reply_markup=markup)
    
@bot.callback_query_handler()
async def startbuttons(msg):
    if msg.data == 'questionData':
        pass 
    elif msg.data == 'profileData':
        pass
    elif msg.data == 'questionList':
        pass
    elif msg.data == 'notificationsSubscription':
        pass
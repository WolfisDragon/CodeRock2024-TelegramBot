from app.models import Profile, Tag, Question, Admin, Answer

def adduser(msg):
  Profile.objects.get_or_create(chatId = msg.chat.id, defaults= {'username': msg.chat.username } )

from app.models import Profile, Tag, Question, Admin, Answer

def adduser(msg):
  Profile.objects.get_or_create(chatId = msg.chat.id, defaults= {'username': msg.chat.username })

def addQuestion(msg):
  Question.objects.create(text = msg.text)

def getprofile(msg):
  for userProfile in Profile.objects.values_list('chatId', 'username').filter(chatId = msg.chat.id):
    return userProfile

def getQuestion():
  qustionList = []
  for qustion in Question.objects.values_list('text').all():
    qustionList += qustion
  return qustionList

def addAnswer(msg, callmsg):
  Answer.objects.create(text=msg.text, questionId = Question.objects.get(text=callmsg))
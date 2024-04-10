from app.models import Profile, Tag, Question, Admin, Answer

def adduser(msg):
  Profile.objects.get_or_create(chatId = msg.chat.id, defaults= {'username': msg.chat.username })

def addQuestion(msg):
  Question.objects.create(text = msg.text)

def getprofile(msg):
  for userProfile in Profile.objects.values_list('chatId', 'username').filter(chatId = msg.chat.id):
    return userProfile

def getQuestion():
  questionList = []
  for question in Question.objects.values_list('text').filter(isModerate= True):
    questionList += question
  return questionList

def addAnswer(msg, callmsg):
  Answer.objects.create(text=msg.text, questionId = Question.objects.get(text=callmsg))
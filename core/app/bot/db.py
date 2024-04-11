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
  for question in Question.objects.values_list('text'):
    questionList += question
  return questionList

def addAnswer(msg, callmsg):
  Answer.objects.create(text=msg.text, questionId = Question.objects.get(text=callmsg))

def viewAnswer(callmsg):
  answerList = []
  for answer in Answer.objects.values_list('text').filter(questionId = Question.objects.get(text=callmsg)):
    answerList += answer
  return answerList
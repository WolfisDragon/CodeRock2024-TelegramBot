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
  for question in Question.objects.values_list('text').filter(isModerate=True):
    questionList += question
  return questionList

def addAnswer(msg, callmsg):
  Answer.objects.create(text=msg.text, questionId = Question.objects.get(text=callmsg))

def viewAnswer(callmsg):
  answerList = []
  for answer in Answer.objects.values_list('text').filter(questionId = Question.objects.get(text=callmsg), isModerate=True):
    answerList += answer
  return answerList

def checkLog(msg):
  for login in Admin.objects.values_list('login').filter(chatId = Profile.objects.get(chatId = msg.chat.id)):
    print(login, msg.text)
    if msg.text == login[0]:
      return True
  return False


def checkPass(msg):
  for password in Admin.objects.values_list('password').filter(chatId = Profile.objects.get(chatId = msg.chat.id)):
    if msg.text == password[0]:
      return True
  return False

def viewQuestionsToModerate():
  qList = []
  for q in Question.objects.values_list('text').filter(isModerate=False):
    qList += q
  return qList

def viewAnswersToModerate():
  answerList = []
  for answer in Answer.objects.values_list('text').filter(isModerate=False):
    answerList += answer
  return answerList

def getQ(msg):
  return Question.objects.get(text=msg.text)
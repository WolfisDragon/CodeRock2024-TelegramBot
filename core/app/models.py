from django.db import models


class Profile(models.Model):
  chatId = models.PositiveBigIntegerField(verbose_name = "ID пользователя", unique = True)
  username = models.CharField(max_length = 50, verbose_name = "Имя Пользователя")


  def __str__(self):
    return f'{self.chatId} {self.username}'
  
  class Meta:
    verbose_name = "Пользователь"
    verbose_name_plural = "Пользователи"

class Question(models.Model):
  text = models.TextField(max_length=300)
  tagId = models.CharField(max_length=50)
  isModerate = models.BooleanField()

  class Meta:
    verbose_name = "Вопрос"
    verbose_name_plural = "Вопросы"

class Answer(models.Model):
  text = models.TextField(max_length=300)
  questionId = models.ForeignKey(Question, on_delete=models.DO_NOTHING)

  class Meta:
    verbose_name = "Ответ"
    verbose_name_plural = "Ответы"

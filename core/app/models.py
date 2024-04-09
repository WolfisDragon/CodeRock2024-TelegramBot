from django.db import models

# Create your models here.
class Profile(models.Model):
  chatId = models.PositiveBigIntegerField(verbose_name = "ID пользователя", unique = True)
  username = models.CharField(max_length = 50, verbose_name = "Имя Пользователя")


  def __str__(self):
    return f'{self.chatId} {self.username}'
  
  class Meta:
    verbose_name = "Пользователь"
    verbose_name_plural = "Пользователи"

class Question(models.Model):
  text = models.TextField()
  tagId = models.CharField()
  isModerate = models.BooleanField()

  class Meta:
    verbose_name = "Вопрос"
    verbose_name_plural = "Вопросы"

class Answer(models.Model):
  text = models.TextField()
  questionId = models.ForeignKey(Question, on_delete=models.DO_NOTHING)

  class Meta:
    verbose_name = "Ответ"
    verbose_name_plural = "Ответы"
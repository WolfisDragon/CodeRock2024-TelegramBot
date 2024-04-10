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
  
class Tag(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.name}'

  class Meta:
    verbose_name = "Тег"
    verbose_name_plural = "Теги"


class Question(models.Model):
  text = models.TextField(max_length=300)
  tagId = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
  isModerate = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.text}'

  class Meta:
    verbose_name = "Вопрос"
    verbose_name_plural = "Вопросы"

class Answer(models.Model):
  text = models.TextField(max_length=300)
  questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
  isModerate = models.BooleanField(default=False)

  def __str__(self):
    return f'{self.text}'

  class Meta:
    verbose_name = "Ответ"
    verbose_name_plural = "Ответы"

class Admin(models.Model):
  chatId = models.OneToOneField(Profile, on_delete=models.CASCADE)
  login = models.CharField(max_length=50)
  password = models.CharField(max_length=100)

  class Meta:
    verbose_name = "Администратор"
    verbose_name_plural = "Администраторы"

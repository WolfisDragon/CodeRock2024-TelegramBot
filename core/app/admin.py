from django.contrib import admin
from app.models import Profile, Tag, Question, Admin, Answer

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['chatId', 'username']

@admin.register(Tag)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['name']

@admin.register(Question)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['text', 'tagId', 'isModerate']

@admin.register(Answer)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['text', 'questionId', 'isModerate']

@admin.register(Admin)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['chatId', 'login', 'password']

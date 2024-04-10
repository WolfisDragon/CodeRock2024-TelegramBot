# Generated by Django 5.0.2 on 2024-04-10 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='isModerate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='questionId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='isModerate',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('chatId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
            ],
            options={
                'verbose_name': 'Администратор',
                'verbose_name_plural': 'Администраторы',
            },
        ),
        migrations.AlterField(
            model_name='question',
            name='tagId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.tag'),
        ),
    ]

import datetime

from django.db import models
from django.utils import timezone


# Вопросы
class Question(models.Model):
    # Текстовое поле с максимальной длинной 200 символов
    question_text = models.CharField(max_length=200)
    # Поле с датой публикации
    pub_date = models.DateTimeField("date published")

    # Коректное предстовление объекта Question
    def __str__(self):
        return self.question_text

    # Пользовательский метод определяющий был ли недавно опубликован опрос
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# Выбор
class Choice(models.Model):
    # Внешний ключ с моделью Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Текст выбора с максимальной длинной 200 символов
    choice_text = models.CharField(max_length=200)
    # Результат голосования целочисленный тип по умолчанию 0
    votes = models.IntegerField(default=0)

    # Коректное предстовление объекта Choice
    def __str__(self):
        return self.choice_text

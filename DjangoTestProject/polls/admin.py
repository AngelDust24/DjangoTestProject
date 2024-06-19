from django.contrib import admin

from .models import Question

# Сообщаем что у объектов Question есть интерфейс администратора
admin.site.register(Question)

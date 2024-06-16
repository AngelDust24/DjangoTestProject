from django.urls import path

from . import views


urlpatterns = [
    # Ссылка на страницу индекс опросов
    # polls/
    path("", views.index, name="index"),
]

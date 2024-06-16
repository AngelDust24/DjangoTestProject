from django.http import HttpResponse


# Приедставление для индекса опросов
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

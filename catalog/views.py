from django.shortcuts import render


def home(request):
    """ Загрузка шаблона домашней страницы."""

    return render(request, "home.html")


def contacts(request):
    """ Загрузка шаблона страницы с контактными данными."""

    return render(request, "contacts.html")

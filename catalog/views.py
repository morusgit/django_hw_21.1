from django.shortcuts import render


def index(request):  # Отображаем шаблон
    return render(request, 'catalog/index.html')  # Отображаем шаблон


def contacts(request):
    if request.method == 'POST':  # Проверяем, была ли отправлена форма
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name}, {email}, {message}')
    return render(request, 'catalog/contacts.html')  # Отображаем шаблон
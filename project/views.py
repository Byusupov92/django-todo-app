from django.shortcuts import render, get_object_or_404, redirect  # Импортируем инструменты для работы с шаблонами
from .models import Task  # Импортируем нашу модель Task
from django.http import HttpResponse  # Импортируем HttpResponse
from .forms import TaskForm 

def home(request):
    return HttpResponse("Привет, это моя первая страница в Django!")  # Возвращаем текст

def task_list(request):
    """ Функция показывает все задачи на странице """
    tasks = Task.objects.all()  # Получаем все записи из базы данных
    return render(request, 'task_list.html', {'tasks': tasks})  # Передаём список задач в шаблон

def task_detail(request, task_id):
    """ Функция показывает одну конкретную задачу по её ID """
    task = get_object_or_404(Task, id=task_id)  # Получаем задачу или показываем ошибку 404
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    """ Функция создаёт новую задачу (пока без формы, добавим позже) """
    if request.method == "POST":  # Если пользователь отправил данные
        title = request.POST['title']  # Получаем заголовок из формы
        description = request.POST['description']  # Получаем описание
        Task.objects.create(title=title, description=description)  # Создаём новую задачу
        return redirect('task_list')  # Перенаправляем на список задач
    return render(request, 'task_create.html')  # Показываем пустую форму

def task_edit(request, task_id):
    """ Функция редактирует задачу """
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_edit.html', {'form': form})

def task_delete(request, task_id):
    """ Функция удаляет задачу """
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'task_delete.html', {'task': task})

from django.contrib import admin  
from .models import Task  # Импортируем нашу модель

# Регистрируем модель, чтобы видеть её в админке
admin.site.register(Task)

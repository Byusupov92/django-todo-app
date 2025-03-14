from django.db import models  # Импортируем модели Django (это класс для создания таблиц в БД)

class Task(models.Model):  
    """ 
    Класс Task создаёт таблицу в базе данных с тремя колонками:
    - title (Заголовок задачи)
    - description (Описание задачи)
    - created_at (Дата и время создания)
    """
    title = models.CharField(max_length=200)  # Поле с ограничением в 200 символов (для заголовка)
    description = models.TextField()  # Поле без ограничений (для описания)
    created_at = models.DateTimeField(auto_now_add=True)  # Автоматически ставит дату создания

    def __str__(self):
        """ Возвращает название задачи в виде строки """
        return self.title  

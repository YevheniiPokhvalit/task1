from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    description = models.TextField(blank=True, verbose_name='Опис категорії')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')

class Task(models.Model):
    PRIORITY_CHOICES = [('low', 'Низький'), ('medium', 'Середній'),('high', 'Високий') ]

    title = models.CharField(max_length=200, verbose_name='Заголовок завдання')
    description = models.TextField(verbose_name='Опис завдання')
    status = models.CharField(max_length=50, default='new', verbose_name='Статус завдання')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення завдання')
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Термін виконання')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name='Пріоритет')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')

    

    



                            
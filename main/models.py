from django.db import models


class Theme(models.Model):
    title = models.CharField('Тема', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class Task(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    date = models.DateField('Дата')
    time = models.TimeField('Время')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



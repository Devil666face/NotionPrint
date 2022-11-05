from django.db import models
from django.urls import reverse


class Typing(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Тип задачи')

    def __str__(self) -> str:
        return self.title

    # def get_absolute_url(self):
    #     return reverse('type',kwargs={'typing_id':self.pk})

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['title']


class Task(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Заголовок задачи')
    content = models.TextField(blank=True, verbose_name='Текст задачи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    appoint_to = models.DateField(verbose_name='Назначено на')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, verbose_name='Прикрепленное фото')
    active = models.BooleanField(default=True, verbose_name='Активна')
    typing = models.ForeignKey('Typing', on_delete=models.PROTECT, null=True, verbose_name='Тип задачи')

    
    def __str__(self) -> str:
        return self.title

    # def get_absolute_url(self):
    #     return reverse('task', kwargs={"pk":self.pk})

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']


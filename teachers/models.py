from django.db import models

class Discipline(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название дисциплины')
    description = models.TextField(blank=True, verbose_name='Описание')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    email = models.EmailField(blank=True, verbose_name='Email')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    disciplines = models.ManyToManyField(Discipline, related_name='teachers', verbose_name='Дисциплины')
    
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'.strip()
    
    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'.strip()
    
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
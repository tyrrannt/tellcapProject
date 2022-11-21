from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class UnitChildModel(models.Model):

    title = models.CharField(default='', max_length=250)
    description = RichTextField(verbose_name='Описание', blank=True)
    is_active = models.BooleanField(db_index=True, verbose_name='Активна', default=True)
    #author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    #created = models.DateField(verbose_name='Дата создания', auto_created=True, null=False)

    def __str__(self):
        return f'{self.title}'


class UnitMainModel(models.Model):

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    title = models.CharField(default='', max_length=250)
    context = models.ManyToManyField(UnitChildModel)

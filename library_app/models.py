from django.db import models

# Create your models here.

class UnitBaseModel(models.Model):
    """
    Абстрактная модель договоров. Введена для возможности реализации иерархической вложенности. Элемент модели
    может выступать в качестве родителя и дочернего объекта.
    """

    class Meta:
        abstract = True

    parent_category = models.ForeignKey('self', verbose_name='Главный документ', on_delete=models.CASCADE, null=True,
                                        blank=True)
    title = models.CharField(default='', max_length=250)

    def __str__(self):
        if self.parent_category:
            return f'{self.parent_category} / {self.title}'
        return f'{self.title}'


class UnitModel(UnitBaseModel):

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

    def __init__(self, *args, **kwargs):
        super(UnitModel, self).__init__(*args, **kwargs)

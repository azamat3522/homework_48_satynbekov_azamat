from django.db import models

CATEGORY_CHOISES = [
    ('other', 'Другое'),
    ('phone', 'Телефон'),
    ('shoes', 'Обувь'),
    ('food', 'Еда'),
    ('clothes', 'Одежда')
]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=50, null=False, blank=False, choices=CATEGORY_CHOISES, default='other',
                                verbose_name='Категория')
    balance = models.IntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name

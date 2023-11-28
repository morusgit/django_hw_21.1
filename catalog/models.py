from django.db import models

# Create your models here.
NULLABLE = {
    'null': True, 'blank': True
}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=200, **NULLABLE, verbose_name='описание')

    def __str__(self):
        # Строковое представление объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    photo = models.ImageField(upload_to='photos/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(**NULLABLE, verbose_name='цена за покупку')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    address = models.CharField(max_length=255, verbose_name='адрес')
    phone = models.CharField(max_length=100, verbose_name='телефон')
    email = models.EmailField(verbose_name='email')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='название'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='название'
    )
    descr = models.CharField(
        max_length=2048,
        verbose_name='описание'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='картинка'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Contact(models.Model):
    name = models.CharField(max_length=64, verbose_name='имя')
    email = models.EmailField(verbose_name='почта')
    subject = models.CharField(max_length=64, verbose_name='причина')
    message = models.CharField(max_length=1024, verbose_name='сообшение')
    date_created = models.DateTimeField(default=now, verbose_name='дата обращения')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'blog_contact'
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ['date_created']



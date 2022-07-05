from django.db import models
from django.urls import reverse


class Book(models.Model):
    #Тип обложки
    SOFT_COVER = 'sf'
    HARD_COVER = 'hd'
    COVER_CHOICE = [
        (SOFT_COVER, 'Мягкая обложка'),
        (HARD_COVER, 'Твердая обложка')
    ]

    #Состояние
    GOOD_CONDITION = 'gd'
    AVERAGE_CONDITION = 'av'
    POOR_CONDITION = 'pr'
    CONDITION_CHOICE = [
        (GOOD_CONDITION, 'Хорошее'),
        (AVERAGE_CONDITION, 'Среднее'),
        (POOR_CONDITION, 'Плохое')
    ]

    title = models.CharField(max_length=150, verbose_name='Название')
    year = models.CharField(max_length=4, blank=True, verbose_name='Год выпуска')
    # author = models.CharField(max_length=150, blank=True, verbose_name='Автор')
    author = models.ManyToManyField('Author', verbose_name='Автор', blank=True,
                                    related_name='book_author')
    # series = models.CharField(max_length=150, blank=True, verbose_name='Серия')
    series = models.ForeignKey('Series', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Серия')
    # pub_house = models.CharField(max_length=150, blank=True, verbose_name='Издательство')
    pub_house = models.ManyToManyField('PubHouse', verbose_name='Издательство', blank=True, related_name='book_series')
    annotation = models.TextField(blank=True, verbose_name='Аннотация')
    condition = models.CharField(max_length=150, choices=CONDITION_CHOICE, verbose_name='Состояние')
    cover = models.CharField(max_length=2, choices=COVER_CHOICE, verbose_name='Обложка')
    price = models.FloatField(blank=True, verbose_name='Цена')
    col_page = models.IntegerField(blank=True, verbose_name='Количество страниц')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home') #, kwargs={'pk': self.pk})


class PubHouse(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    # book = models.ManyToManyField('Book')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name




# Generated by Django 4.0.5 on 2022-07-01 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PubHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('year', models.CharField(blank=True, max_length=4, verbose_name='Год выпуска')),
                ('annotation', models.TextField(blank=True, verbose_name='Аннотация')),
                ('condition', models.CharField(choices=[('gd', 'Хорошее'), ('av', 'Среднее'), ('pr', 'Плохое')], max_length=150, verbose_name='Состояние')),
                ('cover', models.CharField(choices=[('sf', 'Мягкая обложка'), ('hd', 'Твердая обложка')], max_length=2, verbose_name='Обложка')),
                ('price', models.FloatField(blank=True, verbose_name='Цена')),
                ('col_page', models.IntegerField(blank=True, verbose_name='Количество страниц')),
                ('author', models.ManyToManyField(blank=True, related_name='book_author', to='books.author', verbose_name='Автор')),
                ('pub_house', models.ManyToManyField(blank=True, related_name='book_series', to='books.pubhouse', verbose_name='Издательство')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.series', verbose_name='Серия')),
            ],
        ),
    ]

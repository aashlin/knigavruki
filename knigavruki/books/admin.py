from django.contrib import admin
from .models import Book, Author, Series, PubHouse

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Series)
admin.site.register(PubHouse)


from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Book


class Home(ListView):
    model = Book
    template_name = 'books/home.html'




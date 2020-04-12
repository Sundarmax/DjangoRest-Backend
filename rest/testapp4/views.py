from django.shortcuts import render
from .models import Book


def ModelManager():
    BookIns = Book.objects.all()
    print(BookIns)
    # Calling model manager function. 
    Book_Ins = Book.objects.title_count(keyword="maths")
    print(Book_Ins)

#ModelManager()
